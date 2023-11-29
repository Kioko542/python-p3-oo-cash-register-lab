#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.last_transaction = item_cost
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            result = f"After the discount, the total comes to ${self.total:.2f}."
        else:
            result = "There is no discount to apply."
        
        print(result)  # Print the result for debugging purposes
        return result + '\n'

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

