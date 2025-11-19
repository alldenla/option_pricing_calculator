import pytest
from option_pricing.core.monte_carlo import mc_price


class TestMonteCarlo:
    def test_call_option(self):
        """Test call option pricing with Monte Carlo"""
        price = mc_price(S=100, K=100, T=1, r=0.05, sigma=0.2, num_simulations=10000, option_type=1)
        assert isinstance(price, float)
        assert price > 0
        
    def test_put_option(self):
        """Test put option pricing with Monte Carlo"""
        price = mc_price(S=100, K=100, T=1, r=0.05, sigma=0.2, num_simulations=10000, option_type=0)
        assert isinstance(price, float)
        assert price > 0
        
    def test_deep_itm_call(self):
        """Test deep in-the-money call"""
        price = mc_price(S=120, K=100, T=1, r=0.05, sigma=0.2, num_simulations=10000, option_type=1)
        assert price > 15  # Should be worth at least intrinsic value discounted
        
    def test_deep_otm_call(self):
        """Test deep out-of-the-money call"""
        price = mc_price(S=80, K=100, T=1, r=0.05, sigma=0.2, num_simulations=10000, option_type=1)
        assert price < 5  # Should be relatively cheap
