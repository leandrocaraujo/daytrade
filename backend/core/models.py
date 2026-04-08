from pydantic import BaseModel
from datetime import datetime

class AssetCreate(BaseModel):
    ticker: str
    name: str
    market: str

class PriceCreate(BaseModel):
    ticker: str
    price: float
    volume: int
    timestamp: datetime

class Decision(BaseModel):
    ticker: str
    decision: str
    reason: str
    timestamp: datetime
