# store_updated.py

def price_with_discount(product, discount):
    if 0 < discount < 1:
        new_price = int(product["price"] * (1 - discount))
        return new_price
    raise ValueError("discount expects a value between 0 and 1")
