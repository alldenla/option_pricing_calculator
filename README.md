# Option Pricing Calculator

A comprehensive option pricing application featuring multiple pricing models with an interactive GUI.

## Features

- **Multiple Pricing Models:**
  - Black-Scholes (European options)
  - Binomial Tree (European & American options)
  - Monte Carlo Simulation (European options)

- **Performance Optimized:**
  - Numba JIT compilation for Binomial Tree and Monte Carlo
  - Parallel computation for Monte Carlo simulations
  - Real-time calculation updates

- **Interactive GUI:**
  - Built with PySide6 (Qt for Python)
  - Real-time input validation
  - Side-by-side model comparison

## Installation

### Prerequisites
- Python 3.11 or 3.12 or 3.13
- Poetry (for dependency management)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/option-pricing.git
cd option-pricing
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## Usage

### Running the GUI Application

```bash
python -m option_pricing.main
```

Or with poetry:
```bash
poetry run python -m option_pricing.main
```

### Using the Pricing Models Directly

```python
from option_pricing.core import bs_price, bt_price, mc_price

# Black-Scholes
call_price = bs_price(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=1)

# Binomial Tree
put_price = bt_price(S=100, K=100, T=1, r=0.05, sigma=0.2, steps=100, 
                     option_type=0, style='american')

# Monte Carlo
call_price_mc = mc_price(S=100, K=100, T=1, r=0.05, sigma=0.2, 
                         num_simulations=100000, option_type=1)
```

## Project Structure

```
option-pricing/
├── option_pricing/          # Main package
│   ├── controller/          # UI controllers and orchestration
│   │   ├── app.py          # Main application controller
│   │   ├── display_result.py   # Table display manager
│   │   ├── input_parser.py     # Input validation
│   │   ├── pricing_service.py  # Pricing model facade
│   │   └── pricing_params.py   # Data models
│   ├── core/               # Pricing algorithms
│   │   ├── black_scholes.py   # Black-Scholes model
│   │   ├── binomial_tree.py   # Binomial tree model
│   │   └── monte_carlo.py     # Monte Carlo simulation
│   ├── ui/                 # UI components
│   │   ├── calculator.ui      # Qt Designer file
│   │   └── calculator_ui.py   # Generated UI code
│   └── main.py            # Application entry point
├── tests/                  # Unit tests
├── notebooks/              # Jupyter notebooks
├── docs/                   # Documentation
└── examples/               # Example scripts
```

## Parameters

- **S**: Current stock price
- **K**: Strike price
- **T**: Time to maturity (in years)
- **r**: Risk-free interest rate (as decimal, e.g., 0.05 for 5%)
- **sigma**: Volatility (as decimal, e.g., 0.2 for 20%)
- **option_type**: 1 for Call, 0 for Put
- **steps**: Number of time steps for Binomial Tree (1-9999)
- **num_simulations**: Number of simulations for Monte Carlo (1-9999999)
- **style**: 'european' or 'american' (Binomial Tree only)

## Testing

Run the test suite:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest tests/ --cov=option_pricing
```

## Performance Notes

- **First Run Delay**: Numba-optimized functions (Binomial Tree and Monte Carlo) compile on first use, causing a 1-3 second delay. Subsequent calls are extremely fast.
- **Monte Carlo**: Higher simulation counts provide more accuracy but take longer. 100,000+ simulations recommended for production use.
- **Binomial Tree**: More steps provide better convergence. 100-1000 steps typically sufficient.

## Dependencies

- NumPy: Numerical computations
- SciPy: Statistical functions
- PySide6: GUI framework
- Numba: JIT compilation for performance

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Alden - [aldenhjz@gmail.com](mailto:aldenhjz@gmail.com)
