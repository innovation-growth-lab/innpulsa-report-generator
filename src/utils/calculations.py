"""Utils for calculations."""
def calculate_percentage_change(initial: float, final: float) -> str:
    """Calculate percentage change between two values."""
    if initial == 0:
        return "0%"
    return f"{round(((final - initial) / initial) * 100, 1)}%"