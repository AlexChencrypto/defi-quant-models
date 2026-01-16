import math

def calculate_divergence_loss(price_ratio: float) -> float:
    """
    Calculates the Impermanent Loss (Divergence Loss) for a standard 
    Constant Product (x * y = k) AMM pool based on price change.
    
    Args:
        price_ratio (float): The ratio of price change (e.g., 1.50 for 50% increase).
        
    Returns:
        float: The percentage loss compared to holding (e.g., -0.02 for 2% loss).
    """
    if price_ratio <= 0:
        raise ValueError("Price ratio must be positive")
        
    # The standard formula for IL: 2 * sqrt(ratio) / (1 + ratio) - 1
    divergence = (2 * math.sqrt(price_ratio)) / (1 + price_ratio) - 1
    
    return divergence

# Example usage for testing
if __name__ == "__main__":
    # Simulate a 2x price increase (200%)
    ratio = 2.00
    loss = calculate_divergence_loss(ratio)
    
    print(f"--- AMM RISK ANALYSIS ---")
    print(f"Price Change Ratio: {ratio}x")
    print(f"Impermanent Loss: {loss:.4%}")
