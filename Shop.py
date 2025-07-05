from Product import Product
from Customer import Customer
from datetime import datetime
from ShippingService import ShippingService

class Shop:
    def __init__(self):
        self.products = dict()

    def add_product(self, product: Product):
        if product.name in self.products:
            raise ValueError(f"Product {product.name} already exists in the shop.")
        self.products[product.name] = product

    def add_products(self, products: dict[str, Product]):
        for product in products.values():
            self.add_product(product)


    def checkout(self, customer: Customer):

        shippment_cost = ShippingService.shipping_cost(customer.cart.total_shipping_weight())

        if not customer.cart.items:
            raise ValueError("Cart is empty. Cannot checkout.")
        
        total_price = customer.cart.total_price()
        if customer.balance < total_price + shippment_cost:
            raise ValueError("Insufficient balance to complete the purchase.")
        


        # Subtract the quantities of products from the shop's inventory
        for cart_product, cart_quantity in customer.cart.items:
            shop_product = self.products.get(cart_product.name, None)

            if shop_product is None:
                raise ValueError(f"Product {cart_product.name} not found in the shop's inventory.")
            if shop_product.quantity < cart_quantity:
                raise ValueError(f"Insufficient quantity of product {cart_product.name} in the shop's inventory to complete the purchase.")
            if shop_product.is_expired():
                raise ValueError(f"Product {cart_product.name} is expired and cannot be purchased.")
            
            # Deduct the quantity from the shop's inventory
            shop_product.quantity -= cart_quantity

        # Display Receipt
        print("=" * 40)
        print("🧾 Receipt".center(40))
        print("=" * 40)
        print(f"Customer: {customer.name}")
        print("-" * 40)
        print(f"{'Item':<20}{'Qty':>5}{'Price':>15}")
        print("-" * 40)

        for cart_product, cart_quantity in customer.cart.items:
            line_total = cart_product.price * cart_quantity
            print(f"{cart_product.name:<20}{cart_quantity:>5}{line_total:>15.2f}")

        print("-" * 40)
        print(f"{'Cart Subtotal:':<25}${total_price:>10.2f}")
        print(f"{'Shipping Weight:':<25}{customer.cart.total_shipping_weight():>10.2f} kg")
        print(f"{'Shipping Cost:':<25}${shippment_cost:>10.2f}")
        print(f"{'Total Charged:':<25}${(total_price + shippment_cost):>10.2f}")
        print(f"{'Balance After Checkout:':<25}${(customer.balance - (total_price + shippment_cost)):>10.2f}")
        print("=" * 40)



        # Deduct the total price from the customer's balance
        total_cost = total_price + shippment_cost
        customer.balance -= total_cost

        # Create a shipment for the customer
        ShippingService.new_shippment(customer.name, customer.address, customer.cart.total_shipping_weight())
        
        # Clear the cart after successful checkout
        customer.cart.items.clear()
        customer.cart.price = 0.0
        customer.cart.shipping_weight = 0.0
        
        print(f"Checkout successful! {customer.name} has been charged ${total_price + shippment_cost:.2f}.")

