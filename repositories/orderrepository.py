from models.order import Order
import csv
import os


class OrderRepository:

    # Initialization of OrderRepository
    def __init__(self):
        self.__orders = []
        self.__fieldnames = ["ID","UserID","CarCategory","CarID","PayMethod",
                             "PickUpDate","ReturnDate","Status","Deleted"]

    # Function to write order objects into a file
    def orderDictWriter(self, order, file):
        writer = csv.DictWriter(file, self.__fieldnames, restval = "", delimiter=",")
        writer.writerow({'ID'               : order.id,
                         'UserID'           : order.userId,
                         'CarCategory'      : order.carCategory,
                         'CarID'            : order.carId,
                         'PayMethod'        : order.payMethod,
                         'PickUpDate'       : order.pickUpDate,
                         'ReturnDate'       : order.returnDate,
                         'Status'           : order.status,
                         'Deleted'          : order.deleted})

    # Function to open orders.csv and add an instance of order to the end of the file
    def addOrder(self, order):
        isEmpty = not os.path.isfile('./data/orders.csv')
        with open("./data/orders.csv", "a+", newline = '') as orderData:
            if isEmpty:
                csv.writer(orderData).writerow(self.__fieldnames)
            self.orderDictWriter(order, orderData)

    # Function to open orders.csv and overwrite the whole list with an updated list of orders.
    def overwriteOrders(self, orders):
        with open("./data/orders.csv", "w+", newline = '') as orderData:
            csv.writer(orderData).writerow(self.__fieldnames)
            for order in orders:
                self.orderDictWriter(order, orderData)

    def getOrderList(self):
        if self.__orders == []:
            try:
                with open("./data/orders.csv", "r+") as orderData:
                    orderDict = csv.DictReader(orderData)
                    for order in orderDict:
                        newOrder = Order()
                        newOrder.id             = order['ID']
                        newOrder.userId         = order['UserId']
                        newOrder.carCategory    = order['CarCategory']
                        newOrder.carId          = order['CarId']
                        newOrder.payMethod      = order['PayMethod']
                        newOrder.pickUpDate     = order['PickUpDate']
                        newOrder.returnDate     = order['ReturnDate']
                        newOrder.status         = order['Status']
                        newOrder.deleted        = order['Deleted']
                        self.__orders.append(newOrder)
            except FileNotFoundError:
                pass
        return self.__orders
