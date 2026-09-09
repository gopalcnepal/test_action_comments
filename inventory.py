"""Small inventory helper used by the demo test suite."""


def items_to_restock(stock: dict[str, int], threshold: int = 5) -> list[str]:
    """Return the items that are at or below the restock threshold.

    Args:
        stock: Mapping of item name to the quantity currently on hand.
        threshold: Quantity at which an item should be restocked.

    Returns:
        Names of the items needing a restock, in insertion order.
    """
    return [name for name, count in stock.items() if count < threshold]
