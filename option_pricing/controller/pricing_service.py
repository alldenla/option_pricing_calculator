from core import bs_greeks, bt_price, mc_price

class PricingService:
    """Service for pricing options using various models."""
    
    @staticmethod
    def calculate_bs(params: dict[str, float]) -> dict[str, float] | None:
        """Calculate Black-Scholes prices.
        
        Args:
            params: dict with keys S, K, T, r, sigma
        
        Returns:
            dict: {'call': float, 'put': float} or None if error
        """
        try:
            bs_call = bs_greeks(params['S'], params['K'], params['T'], params['r'], params['sigma'], 1)
            bs_put = bs_greeks(params['S'], params['K'], params['T'], params['r'], params['sigma'], 0)
            return {'call': round(bs_call['Price'],4), 'put': round(bs_put['Price'],4)}
        except Exception:
            return None
        
    @staticmethod
    def calculate_bt(params: dict[str, float], time_steps: int, style: str) -> dict[str, float] | None:
        """Calculate Binomial Tree prices.
        
        Args:
            params: dict with keys S, K, T, r, sigma
            time_steps: int
            style: 'american' or 'european'
        
        Returns:
            dict: {'call': float, 'put': float} or None if error
        """
        try:
            bt_call = bt_price(params['S'], params['K'], params['T'], params['r'], params['sigma'], time_steps, 1, style=style)
            bt_put = bt_price(params['S'], params['K'], params['T'], params['r'], params['sigma'], time_steps, 0, style=style)
            return {'call': round(bt_call,4), 'put': round(bt_put,4)}
        except Exception:
            return None
    
    @staticmethod
    def calculate_mc(params: dict[str, float], num_sim: int) -> dict[str, float] | None:
        """Calculate Monte Carlo prices.
        
        Args:
            params: dict with keys S, K, T, r, sigma
            num_sim: int
        
        Returns:
            dict: {'call': float, 'put': float} or None if error
        """
        try:
            mc_call = mc_price(params['S'], params['K'], params['T'], params['r'], params['sigma'], num_sim, 1)
            mc_put = mc_price(params['S'], params['K'], params['T'], params['r'], params['sigma'], num_sim, 0)
            return {'call': round(mc_call,4), 'put': round(mc_put,4)}
        except Exception:
            return None