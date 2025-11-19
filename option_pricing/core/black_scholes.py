import numpy as np
from math import log, sqrt, exp
from scipy.stats import norm

def bs_price(S, K, T, r, sigma, option_type=1):
    # option_type_int: 1=Call, -1=Put
    
    if T<=0 or sigma <=0:
        if option_type == 1:
            return max(S-K*exp(-r*T), 0)
        else:
            return max(0,K*exp(-r*T)-S)
    
    d1 = (log(S/K) + (r + sigma**2/2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T) 
    
    if option_type == 1:
        return float(S*norm.cdf(d1) - K*exp(-r*T)*norm.cdf(d2))
    else:
        return float(K*exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1))
    
def bs_greeks(S, K, T, r, sigma, option_type=1):
    # option_type_int: 1=Call, -1=Put
    
    results = {"Delta":None, "Gamma":None, "Vega":None, "Theta":None, "Rho":None}
    if T<=0 or sigma <=0:
        price = bs_price(S, K, T, r, sigma, option_type)
        results.update({k: float('nan') for k in results})
        results['Price'] = price
        return results
    d1 = (log(S/K) + (r + sigma**2/2)*T)/(sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    Nd1_ = norm.cdf(-d1)
    Nd2_ = norm.cdf(-d2)
    nd1 = norm.pdf(d1)
    
    
    if option_type == 1:
        delta = Nd1
        theta = -S*nd1*sigma/(2*sqrt(T)) - r*K*exp(-r*T)*Nd2
        rho = K*T*exp(-r*T)*Nd2
    else:
        delta = -Nd1_
        theta = -S*nd1*sigma/(2*sqrt(T)) - r*K*exp(-r*T)*Nd2_
        rho = -K*T*exp(-r*T)*Nd2_
    
    gamma = nd1/(S*sigma*sqrt(T))
    vega = S*sqrt(T)*nd1
    
    results.update({"Delta":float(delta), "Gamma":float(gamma), "Vega":float(vega), "Theta":float(theta), "Rho":float(rho)},)
    results['Price'] = bs_price(S, K, T, r, sigma, option_type)

    return results