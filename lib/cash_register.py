#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.quantity = 0
    self.price = 0
    self.discount = discount
    self.total = 0
    self.items = []

  @property
  def quantity(self):
    return self._quantity
  
  @quantity.setter
  def quantity(self, quantity):
    if isinstance(quantity, int) and quantity >= 0:
      self._quantity = quantity
    else:
      print("The quantity must be an integer greater than 0.")

  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, price):
    if isinstance(price, (int, float)) and price >= 0:
      self._price = price
    else:
      print("The price must be an integer greater than 0.")

  def add_item(self, title, price, quantity=1):
    self.quantity = quantity
    self.price = price
    self.total += price * quantity
    count = 0
    while count < quantity:
      self.items.append(title)
      count += 1
    

  def apply_discount(self):
    if self.discount > 0:
      self.total -= int(self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${self.total}.")
      return self.total
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    count = 0
    while count < self.quantity:
      self.items.pop(-1)
      count += 1
    self.total = self.total - (self.price * self.quantity)

# test = CashRegister()
# test.add_item("apple", 0.99)
# print(test.total)
# test.add_item("tomato", 1.76)
# print(test.total)
# test.void_last_transaction()
# print(test.total)