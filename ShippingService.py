class ShippingService:
    shippments = dict()
    
    def __init__(self):
        pass

    @staticmethod
    def shipping_cost(shipping_weight: float) -> float:
        if shipping_weight <= 0:
            raise ValueError("Shipping weight must be greater than zero.")
        
        # Assuming a flat rate of $10 per kg for shipping
        return shipping_weight * 10.0

    @classmethod
    def new_shippment(cls, customer_name: str, customer_address: str, shipping_weight) -> str:
        if not customer_name or not customer_address:
            raise ValueError("Customer name and address cannot be empty.")
        
        if shipping_weight <= 0:
            raise ValueError("Shipping weight must be greater than zero.")
        
        # Check if the customer already has a shipment
        if customer_name in cls.shippments:
            cls.shippments[customer_name]['weight'] += shipping_weight
            cls.shippments[customer_name]['cost'] = cls.shipping_cost(cls.shippments[customer_name]['weight'])
            return f"Shipment updated for {customer_name} with additional weight {shipping_weight} kg and now he has {cls.shippments[customer_name]['weight']} kg in total that will cost ${cls.shippments[customer_name]['cost']}."

        # Create a new shipment entry
        cls.shippments[customer_name] = {
            'address': customer_address,
            'weight': shipping_weight,
            'cost': cls.shipping_cost(shipping_weight)
        }
        
        return f"Shipment created for {customer_name} at {customer_address} with weight {shipping_weight} kg and will cost ${cls.shippments[customer_name]['cost']}."
    
    @classmethod
    def get_shipment(cls, customer_name: str) -> str:
        if customer_name not in cls.shippments:
            raise ValueError(f"No shipment found for customer {customer_name}.")
        
        shipment = cls.shippments[customer_name]
        return f"Shipment for {customer_name}: Address: {shipment['address']}, Weight: {shipment['weight']} kg, Cost: ${shipment['cost']}."