import pytest
from option_pricing.core.binomial_tree import bt_price


class TestBinomialTree:
    def test_european_call(self):
        """Test European call option pricing"""
        price = bt_price(S=100, K=100, T=1, r=0.05, sigma=0.2, steps=100, option_type=1, style='european')
        assert isinstance(price, float)
        assert price > 0
        
    def test_european_put(self):
        """Test European put option pricing"""
        price = bt_price(S=100, K=100, T=1, r=0.05, sigma=0.2, steps=100, option_type=0, style='european')
        assert isinstance(price, float)
        assert price > 0
        
    def test_american_call(self):
        """Test American call option pricing"""
        price = bt_price(S=100, K=100, T=1, r=0.05, sigma=0.2, steps=100, option_type=1, style='american')
        assert isinstance(price, float)
        assert price > 0
        
    def test_american_put(self):
        """Test American put option pricing"""
        price = bt_price(S=100, K=100, T=1, r=0.05, sigma=0.2, steps=100, option_type=0, style='american')
        assert isinstance(price, float)
        assert price > 0
        
    def test_american_put_premium(self):
        """Test that American put has early exercise premium"""
        european = bt_price(S=100, K=110, T=1, r=0.05, sigma=0.2, steps=100, option_type=0, style='european')
        american = bt_price(S=100, K=110, T=1, r=0.05, sigma=0.2, steps=100, option_type=0, style='american')
        assert american >= european
