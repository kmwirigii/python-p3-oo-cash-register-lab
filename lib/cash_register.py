#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initializes the cash register with an optional discount."""
        self.total = 0  # Initialize total price
        self.discount = discount  # Store discount percentage
        self.items = []  # List to track items
        self.last_transaction = 0  # Track last transaction amount

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register."""
        self.total += price * quantity  # Update total price
        self.items.extend([title] * quantity)  # Add items to list
        self.last_transaction = price * quantity  # Store last transaction amount

    def apply_discount(self):
        """Applies discount to the total price."""
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)  # Apply discount correctly
            print(f"After the discount, the total comes to ${round(self.total)}.")  # Ensure correct formatting
        else:
            print("There is no discount to apply.")  # Ensure correct error message format

    def void_last_transaction(self):
        """Removes the last transaction from the total."""
        self.total -= self.last_transaction  # Subtract last transaction amount
        self.last_transaction = 0  # Reset last transaction

    def get_items(self):
        """Returns a list of all items added to the register."""
        return self.items

    def reset_register(self):
        """Resets the register to its initial state."""
        self.total = 0
        self.items = []
        self.last_transaction = 0