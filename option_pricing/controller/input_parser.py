from typing import Any, Dict

def parse_common_inputs(ui: Any) -> Dict[str, float]:
    """Parse and validate inputs from UI
    
    Returns:
         dict: {'S': float, 'K': float, 'T': float, 'r': float, 'sigma': float}

    Raises:
        ValueError: If any input is invalid or empty.
    """
    try:
        S = float(ui.StockPriceInput.text())
        K = float(ui.StrikeInput.text())
        T = float(ui.TimeInput.text())
        r = float(ui.RiskFreeInput.text())
        sigma = float(ui.sigmaInput.text())
    except ValueError as e:
        raise ValueError("Invalid input: all fields must be numeric.") from e

    if S <= 0 or K <= 0 or T <= 0 or sigma <= 0:
        raise ValueError("Invalid input: S, K, T, and sigma must be positive.")

    return {'S': S, 'K': K, 'T': T, 'r': r, 'sigma': sigma}