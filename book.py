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
        print(f"Book on {self.book_name}")

class Book:
    ordersList = [] #list of all the orders

    def __init__(self, name):
        self.name = name

    def insert_buy(self, quantity, price):
        Book.ordersList.append(Order(self.name, "BUY", quantity, price))
        Book.showing()

    def insert_sell(self, quantity, price):
        sell_order =  Order(self.name, "SELL", quantity, price)
        total_quantity = 0
        for order in Book.ordersList:
            if(order.order_type == "BUY"):
                total_quantity += order.quantity
        if(total_quantity >= quantity):
            while(quantity > 0):
                for order in Book.ordersList:
                    if(order.order_type == "BUY"):
                        if(order.quantity > quantity):
                            print("Execute ", quantity, " at ", order.price, " on ", order.book_name)
                            order.quantity -= quantity
                            quantity = 0
                            break
                        else:
                            print("Execute ", order.quantity, " at ", order.price, " on ", order.book_name)
                            quantity -= order.quantity
                            Book.ordersList.remove(order)
        else:
            Book.ordersList.append(sell_order)
        Book.showing()

    def showing():
        Book.ordersList.sort(key = lambda x: x.price, reverse = True)
        for order in Book.ordersList:
            print(f"         {order.order_type} {order.quantity}@{order.price} id={order.number}")
