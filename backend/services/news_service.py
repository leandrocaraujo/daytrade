from datetime import datetime
from typing import List
import os
import xml.etree.ElementTree as ET

import httpx


class NewsService:
    """Serviço para buscar e classificar notícias de mercado."""

    POSITIVE_KEYWORDS = {
        "up",
        "gain",
        "beats",
        "surge",
        "strong",
        "growth",
        "record",
        "buy",
        "bullish",
        "alta",
        "lucro",
        "cresce",
        "positivo",
    }
    NEGATIVE_KEYWORDS = {
        "down",
        "drop",
        "misses",
        "fall",
        "weak",
        "loss",
        "sell",
        "bearish",
        "baixa",
        "queda",
        "prejuizo",
        "negativo",
        "risco",
    }

    @staticmethod
    def classify_sentiment(title: str) -> str:
        lowered = title.lower()
        positive_hits = sum(1 for term in NewsService.POSITIVE_KEYWORDS if term in lowered)
        negative_hits = sum(1 for term in NewsService.NEGATIVE_KEYWORDS if term in lowered)

        if positive_hits > negative_hits:
            return "POSITIVE"
        if negative_hits > positive_hits:
            return "NEGATIVE"
        return "NEUTRAL"

    @staticmethod
    def _build_google_news_rss_url(ticker: str, name: str) -> str:
        query = f"{ticker} {name} stock"
        query = query.strip().replace(" ", "+")
        return f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    @staticmethod
    async def fetch_news_for_asset(ticker: str, name: str, limit: int = 10) -> List[dict]:
        timeout = float(os.getenv("NEWS_PROVIDER_TIMEOUT_SECONDS", "10"))
        url = NewsService._build_google_news_rss_url(ticker=ticker, name=name)

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(url)
            response.raise_for_status()
            xml_text = response.text

        root = ET.fromstring(xml_text)
        channel = root.find("channel")
        if channel is None:
            return []

        items = channel.findall("item")
        news = []

        for item in items[:limit]:
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            pub_date = (item.findtext("pubDate") or "").strip()
            source = (item.findtext("source") or "Google News").strip()

            try:
                parsed_date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
            except ValueError:
                parsed_date = datetime.utcnow()

            news.append(
                {
                    "ticker": ticker.upper(),
                    "title": title,
                    "url": link,
                    "published_at": parsed_date.isoformat(),
                    "source": source,
                    "sentiment": NewsService.classify_sentiment(title),
                }
            )

        return news
