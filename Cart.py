from Product import Product

class Cart:
    def __init__(self):
        self.items = []
        self.price = 0.0
        self.shipping_weight = 0.0

    def add(self, product: Product, quantity: int=1):
        # Check that the product is in the shop's inventory
        if product.get_quantity() < quantity:
            raise ValueError("Insufficient quantity of product to add to cart.")
        
        # If the product is not in the cart, add it
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        

        # Check if the product is already in the cart
        for i, (cart_product, cart_quantity) in enumerate(self.items):
            if cart_product == product:
                # just update the quantity
                self.items[i] = (cart_product, cart_quantity + quantity)
                self.price += product.get_price() * quantity
                self.shipping_weight += product.get_shipping_weight() * quantity
                return
            
        self.items.append((product, quantity))
        self.price += product.get_price() * quantity
        self.shipping_weight += product.get_shipping_weight() * quantity

    def remove_item(self, product: Product, quantity: int=1):

        for i, (cart_product, cart_quantity) in enumerate(self.items):
            if cart_product == product:

                # Check if the quantity to remove is valid
                if cart_quantity < quantity:
                    raise ValueError("Insufficient quantity of product in cart to remove.\nCart_quantity is less than the quantity you want to remove.")
                
                # Adjust the total price and shipping weight
                self.price -= cart_product.get_price() * quantity
                self.shipping_weight -= cart_product.get_shipping_weight() * quantity

                # Adjust the quantity or remove the item from the cart
                if cart_quantity > quantity:
                    self.items[i] = (cart_product, cart_quantity - quantity)
                    break
                if cart_quantity == quantity:
                    del self.items[i]
                    break

    def total_price(self):
        return self.price
    def total_shipping_weight(self):
        return self.shipping_weight
