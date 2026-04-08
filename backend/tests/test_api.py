from typing import Generator
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from backend.app.main import app
from backend.database.models import Base
from backend.database.session import get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_login():
    response = client.post(
        "/api/auth/login",
        params={"email": "user@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_invalid():
    response = client.post(
        "/api/auth/login",
        params={"email": "user@example.com", "password": "wrong"}
    )
    assert response.status_code == 401

def test_create_asset():
    response = client.post(
        "/api/assets",
        json={"ticker": "PETR4", "name": "Petrobras PN", "market": "B3"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Ativo cadastrado com sucesso"

def test_get_assets():
    client.post(
        "/api/assets",
        json={"ticker": "VALE3", "name": "Vale ON", "market": "B3"}
    )
    response = client.get("/api/assets")
    assert response.status_code == 200
    assert len(response.json()["assets"]) > 0

def test_ingest_price():
    client.post(
        "/api/assets",
        json={"ticker": "BBAS3", "name": "Banco do Brasil", "market": "B3"}
    )
    
    response = client.post(
        "/api/prices",
        json={
            "ticker": "BBAS3",
            "price": 30.50,
            "volume": 100000,
            "timestamp": "2026-04-08T10:00:00"
        }
    )
    assert response.status_code == 200
    assert "analysis" in response.json()

def test_get_decision():
    client.post(
        "/api/assets",
        json={"ticker": "ITUB4", "name": "Itaú PN", "market": "B3"}
    )
    
    for price in [100, 101, 102, 101, 100, 99, 100, 101, 102]:
        client.post(
            "/api/prices",
            json={
                "ticker": "ITUB4",
                "price": price,
                "volume": 50000,
                "timestamp": "2026-04-08T10:00:00"
            }
        )
    
    response = client.get("/api/decision/ITUB4")
    assert response.status_code == 200
    assert "decision" in response.json()
    assert response.json()["decision"] in ["BUY", "SELL", "HOLD"]

def test_get_prices():
    client.post(
        "/api/assets",
        json={"ticker": "MGLU3", "name": "Magazine Luiza", "market": "B3"}
    )
    
    client.post(
        "/api/prices",
        json={
            "ticker": "MGLU3",
            "price": 10.50,
            "volume": 500000,
            "timestamp": "2026-04-08T10:00:00"
        }
    )
    
    response = client.get("/api/prices/MGLU3")
    assert response.status_code == 200
    assert response.json()["ticker"] == "MGLU3"
    assert response.json()["count"] > 0
