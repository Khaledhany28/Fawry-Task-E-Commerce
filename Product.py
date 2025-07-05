from datetime import datetime

class Product:
    def __init__(self, name: str, price: float, quantity: int, expiration_date: datetime=None, shipping_weight: float = 0.0):
        
        if price <= 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("quantity cannot be negative.")
        if shipping_weight < 0:
            raise ValueError("Shipping weight cannot be negative.")
        if expiration_date is not None and expiration_date < datetime.now():
            raise ValueError("Expiration date cannot be in the past.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.shipping_weight = shipping_weight

    def is_expired(self):
        if self.expiration_date is None:
            return False
        
        return datetime.now() >= self.expiration_date
    

    ### Getters for the attributes
    def get_shipping_weight(self):
        return self.shipping_weight
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity
    def get_expiration_date(self):
        return self.expiration_date
    

    def __str__(self):
        return self.name
    
    def __eq__(self, value):
        if isinstance(value, Product):
            return self.name == value.name
        return False
