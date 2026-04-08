from datetime import datetime
from typing import List

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
