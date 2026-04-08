import pytest
from backend.services.price_service import PriceService

def test_calculate_sma():
    prices = [100, 101, 102, 101, 100, 99, 100, 101, 102, 101]
    sma = PriceService.calculate_sma(prices, window=5)
    
    assert sma > 0
    assert 99 < sma < 103

def test_calculate_sma_small_window():
    prices = [100, 101, 102]
    sma = PriceService.calculate_sma(prices, window=5)
    
    assert sma == (100 + 101 + 102) / 3

def test_generate_decision_buy():
    current_price = 102
    sma = 100
    decision = PriceService.generate_decision(current_price, sma)
    
    assert decision == "BUY"

def test_generate_decision_sell():
    current_price = 98
    sma = 100
    decision = PriceService.generate_decision(current_price, sma)
    
    assert decision == "SELL"

def test_generate_decision_hold():
    current_price = 100.5
    sma = 100
    decision = PriceService.generate_decision(current_price, sma)
    
    assert decision == "HOLD"

def test_analyze_price():
    prices = [100, 101, 102, 101, 100, 99, 100, 101, 102, 101]
    analysis = PriceService.analyze_price("PETR4", prices)
    
    assert analysis["ticker"] == "PETR4"
    assert "current_price" in analysis
    assert "sma_20" in analysis
    assert "decision" in analysis
    assert analysis["decision"] in ["BUY", "SELL", "HOLD"]

def test_analyze_price_empty():
    analysis = PriceService.analyze_price("VALE3", [])
    
    assert analysis["ticker"] == "VALE3"
    assert analysis["decision"] == "HOLD"
    assert analysis["reason"] == "Sem dados"
