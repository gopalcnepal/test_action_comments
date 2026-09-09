from inventory import items_to_restock


def test_items_below_threshold_are_restocked():
    assert items_to_restock({"bolts": 2, "nuts": 9}) == ["bolts"]


def test_items_exactly_at_threshold_are_restocked():
    # "at or below the threshold" includes an item sitting exactly on it.
    assert items_to_restock({"washers": 5, "nuts": 9}) == ["washers"]


def test_empty_stock_needs_no_restock():
    assert items_to_restock({}) == []
