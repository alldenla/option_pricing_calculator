from dataclasses import dataclass

@dataclass
class PricingParams:
    """Data class for option pricing parameters."""
    S: float  # Stock price
    K: float  # Strike price
    T: float  # Time to maturity
    r: float  # Risk-free rate
    sigma: float  # Volatility
