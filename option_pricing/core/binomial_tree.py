import numpy as np
from math import log, sqrt, exp
from numba import njit

@njit(fastmath=True)
def bt_price(S, K, T, r, sigma, steps=100, option_type=1, style='european'):
    # option_type_int: 1=Call, -1=Put
    
    dt = T / steps
    u = exp(sigma * sqrt(dt))
    d = 1 / u
    p = (exp(r * dt) - d) / (u - d)
    discount = exp(-r * dt)

    # Initialize asset prices at maturity
    asset_prices = np.empty(steps + 1)
    for j in range(steps + 1):
        asset_prices[j] = S * (u ** j) * (d ** (steps - j))
   
    # Initialize option values at maturity
    option_values = np.empty(steps + 1)
    if option_type == 1:
        for j in range(steps + 1):
            option_values[j] = max(0.0, asset_prices[j] - K)
    else:
        for j in range(steps + 1):
            option_values[j] = max(0.0, K - asset_prices[j])

    # Backward induction
    is_american = (style == 'american')
    
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            # Calculate discounted expected value
            option_values[j] = discount * (p * option_values[j + 1] + (1 - p) * option_values[j])
            
            # Check early exercise for American options
            if is_american:
                asset_price = S * (u ** j) * (d ** (i - j))
                if option_type == 1:
                    exercise_value = max(0.0, asset_price - K)
                else:
                    exercise_value = max(0.0, K - asset_price)
                option_values[j] = max(option_values[j], exercise_value)
    
    return float(option_values[0])
