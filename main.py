from Product import Product
from Customer import Customer
from datetime import datetime
from Shop import Shop

# Example usage
shop = Shop()

products = {
    "Apple" : Product(name="Apple", price=15, quantity=100, expiration_date=datetime(2025, 12, 31), shipping_weight=0.2),
    "Banana" : Product(name="Banana", price=20, quantity=50, expiration_date=datetime(2026, 6, 15), shipping_weight=0.5),
    "TV" : Product(name="TV", price=10000, quantity=20, shipping_weight=5.0),
    "IPhone" : Product(name="IPhone", price=65000, quantity=30, shipping_weight=0.3),
    "Card" : Product(name="Card", price=10, quantity=100),
}


shop.add_products(products)

# Create a customer and add products to their cart
Khaled = Customer(name="Khaled Hany", address="Cairo, Egypt", balance=100000.0)

Khaled.cart.add(products["Apple"], quantity=2)
Khaled.cart.add(products["Banana"], quantity=3)
Khaled.cart.add(products["TV"], quantity=1)
Khaled.cart.add(products["Card"], quantity=5)


shop.checkout(Khaled)