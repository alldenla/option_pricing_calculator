"""
Basic usage examples for option pricing models
"""

from option_pricing.core.black_scholes import bs_price, bs_greeks
from option_pricing.core.binomial_tree import bt_price
from option_pricing.core.monte_carlo import mc_price


def main():
    # Common parameters
    S = 100      # Stock price
    K = 100      # Strike price
    T = 1        # Time to maturity (1 year)
    r = 0.05     # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)
    
    print("=" * 60)
    print("Option Pricing Examples")
    print("=" * 60)
    print(f"\nParameters:")
    print(f"  Stock Price (S): ${S}")
    print(f"  Strike Price (K): ${K}")
    print(f"  Time to Maturity (T): {T} year")
    print(f"  Risk-free Rate (r): {r*100}%")
    print(f"  Volatility (σ): {sigma*100}%")
    
    # Black-Scholes
    print("\n" + "-" * 60)
    print("BLACK-SCHOLES MODEL (European Options)")
    print("-" * 60)
    
    bs_call = bs_price(S, K, T, r, sigma, option_type=1)
    bs_put = bs_price(S, K, T, r, sigma, option_type=0)
    
    print(f"Call Price: ${bs_call:.4f}")
    print(f"Put Price:  ${bs_put:.4f}")
    
    # Greeks for call option
    greeks = bs_greeks(S, K, T, r, sigma, option_type=1)
    print(f"\nGreeks (Call):")
    print(f"  Delta: {greeks['Delta']:.4f}")
    print(f"  Gamma: {greeks['Gamma']:.4f}")
    print(f"  Vega:  {greeks['Vega']:.4f}")
    print(f"  Theta: {greeks['Theta']:.4f}")
    print(f"  Rho:   {greeks['Rho']:.4f}")
    
    # Binomial Tree - European
    print("\n" + "-" * 60)
    print("BINOMIAL TREE MODEL (European Options)")
    print("-" * 60)
    
    bt_call_euro = bt_price(S, K, T, r, sigma, steps=100, option_type=1, style='european')
    bt_put_euro = bt_price(S, K, T, r, sigma, steps=100, option_type=0, style='european')
    
    print(f"Call Price: ${bt_call_euro:.4f}")
    print(f"Put Price:  ${bt_put_euro:.4f}")
    
    # Binomial Tree - American
    print("\n" + "-" * 60)
    print("BINOMIAL TREE MODEL (American Options)")
    print("-" * 60)
    
    bt_call_amer = bt_price(S, K, T, r, sigma, steps=100, option_type=1, style='american')
    bt_put_amer = bt_price(S, K, T, r, sigma, steps=100, option_type=0, style='american')
    
    print(f"Call Price: ${bt_call_amer:.4f}")
    print(f"Put Price:  ${bt_put_amer:.4f}")
    print(f"\nEarly Exercise Premium (Put): ${bt_put_amer - bt_put_euro:.4f}")
    
    # Monte Carlo
    print("\n" + "-" * 60)
    print("MONTE CARLO SIMULATION (European Options)")
    print("-" * 60)
    print("Note: First run may take a few seconds (Numba compilation)")
    
    mc_call = mc_price(S, K, T, r, sigma, num_simulations=100000, option_type=1)
    mc_put = mc_price(S, K, T, r, sigma, num_simulations=100000, option_type=0)
    
    print(f"Call Price: ${mc_call:.4f}")
    print(f"Put Price:  ${mc_put:.4f}")
    
    # Model Comparison
    print("\n" + "=" * 60)
    print("MODEL COMPARISON (European Call)")
    print("=" * 60)
    print(f"Black-Scholes:   ${bs_call:.4f}")
    print(f"Binomial Tree:   ${bt_call_euro:.4f}")
    print(f"Monte Carlo:     ${mc_call:.4f}")
    
    print("\n")


if __name__ == "__main__":
    main()
