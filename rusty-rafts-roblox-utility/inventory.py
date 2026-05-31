"""
Simple inventory management for raft resources.
"""

class Inventory:
    def __init__(self, max_slots: int = 20):
        self._items = {}
        self._max_slots = max_slots

    def add_item(self, item_name: str, quantity: int = 1) -> bool:
        """Add items to inventory. Returns False if inventory full."""
        if len(self._items) >= self._max_slots and item_name not in self._items:
            return False
        self._items[item_name] = self._items.get(item_name, 0) + quantity
        return True

    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        """Remove items. Returns False if insufficient quantity."""
        current = self._items.get(item_name, 0)
        if current < quantity:
            return False
        if current == quantity:
            del self._items[item_name]
        else:
            self._items[item_name] = current - quantity
        return True

    def get_item_count(self, item_name: str) -> int:
        return self._items.get(item_name, 0)

    def list_items(self) -> dict:
        return dict(self._items)