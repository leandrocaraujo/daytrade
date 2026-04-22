from datetime import datetime
from fastapi import APIRouter, HTTPException, Query
from core.models import AssetCreate, PriceCreate
from services.price_service import PriceService

router = APIRouter(prefix="/api", tags=["assets"])

# Simulado - em produção usar banco de dados
assets_db = {}
prices_db = {}

@router.post("/assets")
async def create_asset(asset: AssetCreate):
    """Cadastra um novo ativo"""
    if asset.ticker in assets_db:
        return {"error": "Ativo já cadastrado"}
    
    assets_db[asset.ticker] = {
        "ticker": asset.ticker,
        "name": asset.name,
        "market": asset.market
    }
    
    prices_db[asset.ticker] = []
    
    return {
        "message": "Ativo cadastrado com sucesso",
        "asset": assets_db[asset.ticker]
    }

@router.post("/prices")
async def ingest_price(price: PriceCreate):
    """Injesta preço de um ativo"""
    if price.ticker not in assets_db:
        return {"error": "Ativo não encontrado"}
    
    prices_db[price.ticker].append({
        "price": price.price,
        "volume": price.volume,
        "timestamp": price.timestamp.isoformat()
    })
    
    # Gera análise técnica
    price_list = [p["price"] for p in prices_db[price.ticker]]
    analysis = PriceService.analyze_price(price.ticker, price_list)
    
    return {
        "message": "Preço ingerido com sucesso",
        "analysis": analysis
    }

@router.get("/decision/{ticker}")
async def get_decision(ticker: str):
    """Retorna decisão para um ativo"""
    if ticker not in assets_db:
        return {"error": "Ativo não encontrado"}
    
    if not prices_db.get(ticker):
        return {
            "ticker": ticker,
            "decision": "HOLD",
            "reason": "Sem dados de preço"
        }
    
    price_list = [p["price"] for p in prices_db[ticker]]
    analysis = PriceService.analyze_price(ticker, price_list)
    
    return analysis

@router.get("/assets")
async def list_assets():
    """Lista todos os ativos cadastrados"""
    return {"assets": list(assets_db.values())}

@router.get("/prices/{ticker}")
async def get_prices(ticker: str, limit: int = 100):
    """Retorna histórico de preços de um ativo"""
    if ticker not in assets_db:
        return {"error": "Ativo não encontrado"}
    
    prices = prices_db.get(ticker, [])
    return {
        "ticker": ticker,
        "count": len(prices),
        "prices": prices[-limit:]
    }


@router.get("/prices/live/{ticker}")
async def get_live_price(
    ticker: str,
    persist: bool = Query(
        default=True,
        description="Quando true, salva o preço buscado no histórico em memória.",
    ),
):
    """Busca preço em provedor real e opcionalmente persiste no histórico."""
    if ticker not in assets_db:
        raise HTTPException(status_code=404, detail="Ativo não encontrado")

    asset = assets_db[ticker]

    try:
        live_quote = await PriceService.fetch_live_price(
            ticker=ticker,
            market=asset["market"],
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Falha ao obter preço em tempo real: {str(exc)}",
        ) from exc

    if persist:
        prices_db[ticker].append(
            {
                "price": live_quote["price"],
                "volume": live_quote["volume"],
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

    price_list = [p["price"] for p in prices_db[ticker]]
    analysis = PriceService.analyze_price(ticker, price_list) if price_list else None

    return {
        "message": "Preço em tempo real obtido com sucesso",
        "quote": live_quote,
        "persisted": persist,
        "analysis": analysis,
    }
