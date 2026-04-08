def test_price_service():
    from backend.services.price_service import PriceService
    
    prices = [100, 101, 102, 101, 100, 99, 100, 101, 102, 101]
    
    sma = PriceService.calculate_sma(prices, window=5)
    assert sma > 0
    
    decision = PriceService.generate_decision(102, sma)
    assert decision in ["BUY", "SELL", "HOLD"]
    
    analysis = PriceService.analyze_price("PETR4", prices)
    assert analysis["ticker"] == "PETR4"
    assert "decision" in analysis
    assert "current_price" in analysis
