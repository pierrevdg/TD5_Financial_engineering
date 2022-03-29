class Order:
    number = 0
    
    def __init__(self, book_name, order_type, quantity, price):
        Order.number += 1
        self.number = Order.number
        self.book_name = book_name
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        print("--------------------------------")
        print(f"--- Insert {self.order_type} {self.quantity}@{self.price} id={self.number} on {self.book_name}")

class Book:
    ordersList = [] #list of all the orders

    def __init__(self, name):
        self.name = name

    def insert_buy(self, quantity, price):
        buy_order = Order(self.name, "BUY", quantity, price)
        for order in Book.ordersList:
            if(order.order_type == "SELL"):
                if(price >= order.price):
                    if(order.quantity > quantity):
                        print("Execute ", quantity, " at ", order.price, " on ", order.book_name)
                        order.quantity -= quantity
                        quantity = 0
                        break
                    else:
                        print("Execute ", order.quantity, " at ", order.price, " on ", order.book_name)
                        quantity -= order.quantity
                        order.quantity = 0
        if(quantity > 0):
            buy_order.quantity = quantity
            Book.ordersList.append(buy_order)
        Book.showing(self)

    def insert_sell(self, quantity, price):
        sell_order =  Order(self.name, "SELL", quantity, price)
        for order in Book.ordersList:
            if(order.order_type == "BUY"):
                if(price <= order.price):
                    if(order.quantity > quantity):
                        print("Execute ", quantity, " at ", order.price, " on ", order.book_name)
                        order.quantity -= quantity
                        quantity = 0
                        break
                    else:
                        print("Execute ", order.quantity, " at ", order.price, " on ", order.book_name)
                        quantity -= order.quantity
                        order.quantity = 0
        if(quantity > 0):
            sell_order.quantity = quantity
            Book.ordersList.append(sell_order)
        Book.showing(self)

    def showing(self):
        print("Book on ", self.name)
        Book.ordersList.sort(key = lambda x: x.price, reverse = True)
        for j in range(0, len(Book.ordersList) - 1):
            for i in range(0, len(Book.ordersList) - 1):
                if(Book.ordersList[i].quantity == 0):
                    del Book.ordersList[i]
        for order in Book.ordersList:
            print(f"         {order.order_type} {order.quantity}@{order.price} id={order.number}")
