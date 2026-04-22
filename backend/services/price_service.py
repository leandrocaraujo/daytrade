from datetime import datetime
from typing import List
import os
import httpx

class PriceService:
    """Serviço para gerenciar preços e análises técnicas"""
    
    @staticmethod
    def calculate_sma(prices: List[float], window: int = 20) -> float:
        """Calcula Média Móvel Simples"""
        if len(prices) < window:
            return sum(prices) / len(prices) if prices else 0
        return sum(prices[-window:]) / window
    
    @staticmethod
    def generate_decision(current_price: float, sma: float) -> str:
        """Gera decisão baseada na comparação com SMA"""
        if current_price > sma * 1.02:
            return "BUY"
        elif current_price < sma * 0.98:
            return "SELL"
        else:
            return "HOLD"
    
    @staticmethod
    def analyze_price(ticker: str, prices: List[float]) -> dict:
        """Analisa preço e retorna decisão"""
        if not prices:
            return {"ticker": ticker, "decision": "HOLD", "reason": "Sem dados"}
        
        current_price = prices[-1]
        sma = PriceService.calculate_sma(prices)
        decision = PriceService.generate_decision(current_price, sma)
        
        return {
            "ticker": ticker,
            "current_price": current_price,
            "sma_20": sma,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        }

    @staticmethod
    def combine_market_and_news_signal(market_decision: str, sentiment_score: int) -> str:
        """
        Combina decisão técnica com sentimento agregado de notícias.
        sentiment_score:
        - positivo -> favorece BUY
        - negativo -> favorece SELL
        - zero -> neutro
        """
        if market_decision == "BUY":
            if sentiment_score < -1:
                return "HOLD"
            return "BUY"

        if market_decision == "SELL":
            if sentiment_score > 1:
                return "HOLD"
            return "SELL"

        # market_decision == HOLD
        if sentiment_score >= 2:
            return "BUY"
        if sentiment_score <= -2:
            return "SELL"
        return "HOLD"

    @staticmethod
    def _format_symbol_for_provider(ticker: str, market: str, provider: str) -> str:
        """Normaliza símbolo por provedor."""
        normalized_ticker = ticker.strip().upper()
        normalized_market = market.strip().upper()

        if provider == "stooq":
            if normalized_market == "B3":
                return f"{normalized_ticker}.SA"
            if normalized_market in {"NASDAQ", "NYSE", "AMEX"}:
                return f"{normalized_ticker}.US"
            return normalized_ticker

        # Alpha Vantage
        if normalized_market == "B3":
            return f"{normalized_ticker}.SAO"
        return normalized_ticker

    @staticmethod
    async def fetch_live_price(ticker: str, market: str) -> dict:
        """
        Busca preço real de mercado.
        Fluxo:
        1) Tenta Alpha Vantage quando API key está configurada.
        2) Faz fallback para Stooq sem autenticação.
        """
        alpha_key = os.getenv("ALPHA_VANTAGE_API_KEY", "").strip()
        timeout = float(os.getenv("PRICE_PROVIDER_TIMEOUT_SECONDS", "10"))

        # Primeiro provedor: Alpha Vantage (quando configurado)
        if alpha_key:
            alpha_symbol = PriceService._format_symbol_for_provider(
                ticker=ticker,
                market=market,
                provider="alpha",
            )
            alpha_url = (
                "https://www.alphavantage.co/query"
                f"?function=GLOBAL_QUOTE&symbol={alpha_symbol}&apikey={alpha_key}"
            )

            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.get(alpha_url)
                    response.raise_for_status()
                    payload = response.json()

                quote = payload.get("Global Quote", {})
                price_raw = quote.get("05. price")
                if price_raw:
                    return {
                        "ticker": ticker.upper(),
                        "market": market.upper(),
                        "provider": "alpha_vantage",
                        "price": float(price_raw),
                        "volume": int(float(quote.get("06. volume", 0))),
                        "timestamp": datetime.utcnow().isoformat(),
                    }
            except Exception:
                # Fallback no próximo provedor
                pass

        # Fallback: Stooq (CSV público)
        stooq_symbol = PriceService._format_symbol_for_provider(
            ticker=ticker,
            market=market,
            provider="stooq",
        ).lower()
        stooq_url = f"https://stooq.com/q/l/?s={stooq_symbol}&f=sd2t2ohlcv&h&e=csv"

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.get(stooq_url)
            response.raise_for_status()
            csv_text = response.text.strip()

        lines = csv_text.splitlines()
        if len(lines) < 2:
            raise ValueError("Resposta inválida do provedor de preços.")

        # Formato esperado:
        # Symbol,Date,Time,Open,High,Low,Close,Volume
        # petr4.sa,2026-04-22,17:00:00,30.1,30.6,29.9,30.5,12345678
        parts = lines[1].split(",")
        if len(parts) < 8 or parts[6] in {"N/D", ""}:
            raise ValueError("Preço indisponível para o ativo informado.")

        return {
            "ticker": ticker.upper(),
            "market": market.upper(),
            "provider": "stooq",
            "price": float(parts[6]),
            "volume": int(float(parts[7] or 0)),
            "timestamp": datetime.utcnow().isoformat(),
        }
