from ShoppingCart import ShoppingCart
def test_shopping_cart():
    cart = ShoppingCart()
    cart.add_item("Apple")
    assert len(cart.items) == 1
    assert cart.items[0] == "Apple"
    cart.add_item("Banana")
    assert len(cart.items) == 2
    assert cart.items[1] == "Banana"
    cart.add_item("Apple")
    assert len(cart.items) == 3
    assert cart.items[2] == "Apple"