from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Plataforma Analítica Financeira",
    description="API para análise de mercado financeiro em tempo real",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à Plataforma Analítica Financeira"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/api/assets")
def create_asset(ticker: str, name: str, market: str):
    return {
        "ticker": ticker,
        "name": name,
        "market": market,
        "message": "Ativo cadastrado com sucesso"
    }

@app.post("/api/prices")
def ingest_price(ticker: str, price: float, volume: int, timestamp: str):
    return {
        "ticker": ticker,
        "price": price,
        "volume": volume,
        "timestamp": timestamp,
        "message": "Preço ingerido com sucesso"
    }

@app.get("/api/decision/{ticker}")
def get_decision(ticker: str):
    return {
        "ticker": ticker,
        "decision": "HOLD",
        "reason": "Análise técnica em processamento"
    }
