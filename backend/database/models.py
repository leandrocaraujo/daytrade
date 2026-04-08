from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Asset(Base):
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), unique=True, index=True)
    name = Column(String(100))
    market = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)

class Price(Base):
    __tablename__ = "prices"
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), index=True)
    price = Column(Float)
    volume = Column(Integer)
    timestamp = Column(DateTime, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Decision(Base):
    __tablename__ = "decisions"
    
    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), index=True)
    decision = Column(String(20))
    reason = Column(String(500))
    timestamp = Column(DateTime, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
