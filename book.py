class Order:
    number = 0
    
    def __init__(self, book_name, order_type, quantity, price):
        Order.number += 1
        self.number = Order.number
        self.book_name = book_name
        self.order_type = order_type
        self.quantity = quantity
        self.price = price

class Book:
    ordersList = [] #list of all the orders

    def __init__(self, name):
        self.name = name

    def insert_buy(self, quantity, price):
        Book.ordersList.append(Order(self.name, "BUY", quantity, price))

    def insert_sell(self, quantity, price):
        Book.ordersList.append(Order(self.name, "SELL", quantity, price))
