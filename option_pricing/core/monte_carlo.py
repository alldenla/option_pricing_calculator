import numpy as np
from math import sqrt, exp
from numba import njit, prange

@njit(parallel=True, fastmath=True)
def mc_price(S, K, T, r, sigma, num_simulations=1000000, option_type=1):
    # option_type_int: 1=Call, -1=Put
    
    dt = T
    drift = (r - 0.5 * sigma**2) * dt
    vol = sigma * sqrt(dt)
    discount_factor = exp(-r * T)
    
    sum_payoffs = 0.0
    
    # Loop over half the simulations due to antithetic variates
    num_half = num_simulations // 2
    
    for i in prange(num_half):
        Z = np.random.standard_normal()
        
        # Calculate asset prices for both Z and -Z
        S_T1 = S * exp(drift + vol * Z)
        S_T2 = S * exp(drift - vol * Z)
        
        if option_type == 1:
            payoff1 = max(0, S_T1 - K)
            payoff2 = max(0, S_T2 - K)
        else:
            payoff1 = max(0, K - S_T1)
            payoff2 = max(0, K - S_T2)
        
        sum_payoffs += payoff1 + payoff2
    
    option_price = discount_factor * (sum_payoffs / num_simulations)
    return float(option_price)