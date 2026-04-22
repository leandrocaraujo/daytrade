from fastapi import APIRouter, HTTPException, Query

from app.routes.assets import assets_db
from services.news_service import NewsService

router = APIRouter(prefix="/api/news", tags=["news"])

# Simulado - em produção usar banco de dados
news_db = {}


@router.get("/live/{ticker}")
async def ingest_live_news(
    ticker: str,
    limit: int = Query(default=10, ge=1, le=50),
    persist: bool = Query(
        default=True,
        description="Quando true, salva as notícias no histórico em memória.",
    ),
):
    """Busca notícias em tempo real e opcionalmente persiste por ativo."""
    if ticker not in assets_db:
        raise HTTPException(status_code=404, detail="Ativo não encontrado")

    asset = assets_db[ticker]
    try:
        fresh_news = await NewsService.fetch_news_for_asset(
            ticker=ticker,
            name=asset["name"],
            limit=limit,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Falha ao obter notícias em tempo real: {str(exc)}",
        ) from exc

    if persist:
        existing = news_db.setdefault(ticker, [])
        existing_urls = {item["url"] for item in existing}
        for item in fresh_news:
            if item["url"] and item["url"] not in existing_urls:
                existing.append(item)
                existing_urls.add(item["url"])

    return {
        "message": "Notícias em tempo real obtidas com sucesso",
        "ticker": ticker,
        "count": len(fresh_news),
        "persisted": persist,
        "news": fresh_news,
    }


@router.get("/{ticker}")
async def list_news_for_ticker(
    ticker: str,
    limit: int = Query(default=20, ge=1, le=200),
):
    """Lista notícias já ingeridas do ativo."""
    if ticker not in assets_db:
        raise HTTPException(status_code=404, detail="Ativo não encontrado")

    records = news_db.get(ticker, [])
    return {
        "ticker": ticker,
        "count": len(records),
        "news": records[-limit:],
    }
