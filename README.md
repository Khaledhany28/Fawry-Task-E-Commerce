# 🛒 Python E-Commerce Simulation
---
To be honest i used chatgpt to create the readme file 👀


This project is a basic simulation of an e-commerce store in Python. It consists of:

- `Product`: Represents a product in the store.
- `Cart`: Holds products selected by the customer.
- `Customer`: Represents a customer with a balance and a shopping cart.
- `ShippingService`: Handles shipment cost calculation and shipment records.
- `Shop`: Manages products and handles the checkout process.

---

## 🧱 Structure Overview

### 1. Product Class

Defines the product with pricing, quantity, expiration date, and shipping weight.

```python
product = Product(
    name="Apple",
    price=15,
    quantity=100,
    expiration_date=datetime(2025, 12, 31),
    shipping_weight=0.2
)
```

### 2. Cart Class

Allows adding/removing products and calculates total price and weight.

```python
cart = Cart()
cart.add(product, quantity=2)
cart.remove(product, quantity=1)
```

### 3. Customer Class

Represents a customer with a name, balance, address, and cart.

```python
customer = Customer(name="Khaled Hany", address="Cairo, Egypt", balance=100000.0)
customer.cart.add(products["TV"], quantity=1)
```

### 4. ShippingService Class

Calculates shipping cost and tracks shipments.

```python
ShippingService.new_shippment(customer.name, customer.address, 5.0)
```

---

## 🏪 Shop Class

Handles inventory and checkout. Validates stock, balance, and expiration before processing an order.

```python
shop = Shop()
shop.add_products({
    "TV": Product("TV", 10000, 20, shipping_weight=5.0),
    "Banana": Product("Banana", 20, 50, expiration_date=datetime(2026, 6, 15), shipping_weight=0.5),
    ...
})
```

---

## ✅ Checkout Flow

1. Customer adds products to cart.
2. Shop verifies availability and balance.
3. Shop deducts inventory and balance.
4. Shipping is calculated.
5. Shipment is registered.
6. Receipt is printed.

```python
shop.checkout(Khaled)
```

### Sample Receipt Output:

```
========================================
              🧾 Receipt               
========================================
Customer: Khaled Hany
----------------------------------------
Item                     Qty         Price
----------------------------------------
Apple                      2           30.00
Banana                     3           60.00
TV                         1        10000.00
Card                       5           50.00
----------------------------------------
Cart Subtotal:           $10140.00
Shipping Weight:          7.10 kg
Shipping Cost:            $71.00
Total Charged:          $10211.00
Balance After Checkout: $89789.00
========================================
Checkout successful! Khaled Hany has been charged $10211.00.
```

---

## 🧪 Example Test Run

```python
shop = Shop()

products = {
    "Apple": Product("Apple", 15, 100, datetime(2025, 12, 31), 0.2),
    "Banana": Product("Banana", 20, 50, datetime(2026, 6, 15), 0.5),
    "TV": Product("TV", 10000, 20, shipping_weight=5.0),
    "Card": Product("Card", 10, 100),
}

shop.add_products(products)

khaled = Customer("Khaled Hany", "Cairo, Egypt", balance=100000.0)
khaled.cart.add(products["Apple"], 2)
khaled.cart.add(products["Banana"], 3)
khaled.cart.add(products["TV"], 1)
khaled.cart.add(products["Card"], 5)

shop.checkout(khaled)
```

![Output screenshot](screenshots\code_output.png)

---

## ✨ Author

**Khaled Hany**