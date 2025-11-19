import pytest
from option_pricing.core.black_scholes import bs_price, bs_greeks


class TestBlackScholes:
    def test_call_option_basic(self):
        """Test basic call option pricing"""
        price = bs_price(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=1)
        assert isinstance(price, float)
        assert price > 0
        
    def test_put_option_basic(self):
        """Test basic put option pricing"""
        price = bs_price(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=0)
        assert isinstance(price, float)
        assert price > 0
        
    def test_greeks_calculation(self):
        """Test Greeks calculation"""
        greeks = bs_greeks(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=1)
        assert 'Price' in greeks
        assert 'Delta' in greeks
        assert 'Gamma' in greeks
        assert 'Vega' in greeks
        assert 'Theta' in greeks
        assert 'Rho' in greeks
        
    def test_put_call_parity(self):
        """Test put-call parity relationship"""
        S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
        call = bs_price(S, K, T, r, sigma, 1)
        put = bs_price(S, K, T, r, sigma, 0)
        import math
        parity_diff = call - put - (S - K * math.exp(-r * T))
        assert abs(parity_diff) < 0.01
