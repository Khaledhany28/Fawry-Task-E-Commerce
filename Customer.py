from Cart import Cart

class Customer:
    def __init__(self, name: str, address: str=None, balance: int=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.name = name
        self.address = address
        self.balance = balance
        self.cart = Cart()

    def add_balance(self, amount: int):
        if amount <= 0:
            raise ValueError("Cannot add negative balance.")
        self.balance += amount

    def change_address(self, new_address: str):
        if not new_address or not isinstance(new_address, str):
            raise ValueError("Address cannot be empty.")
        self.address = new_address


