from typing import List

class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[str] = []

    def add_item(self, item: str) -> None:
        self.items.append(item)

    def size(self) -> int:
        return 0

    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map):
        pass