from models.order import Order
import csv

class OrderRepository:
    
    def __init__(self):
        self.__orders = []
        self.__fieldnames = ["ID","UserID","CarCategory","CarID","Payment Method","PickUpDate","ReturnDate","Status","Deleted"]

        #Function to open cars.csv and add an instance of car to the end of the file
    def addOrder(self, order):
        with open("./data/orders.csv", "a+", newline = '') as orderData:
            self.carDictWriter(order, orderData)
            self.__orders.append(order)


    #Function to open cars.csv and overwrite the whole list with an updated list of cars.
    def overwriteOrders(self, orders):
        with open("./data/orders.csv", "w+", newline = '') as orderData:
            csv.writer(orderData).writerow(self.__fieldnames)
            for order in orders:
                self.carDictWriter(order, orderData)
                
    def getOrderList(self):
        if self.__orders == []:
            with open("./data/orders.csv", "r+") as orderData:
                orderDict = csv.DictReader(orderData)
                for order in orderDict: 
                    newOrder = Order()
                    newOrder.id             = order['ID']
                    newOrder.userId         = order['UserId']
                    newOrder.carCategory    = order['CarCategory']
                    newOrder.carId          = order['CarId']
                    newOrder.payMethod      = order['Payment Method']
                    newOrder.pickUpDate     = order['PickUpDate']
                    newOrder.returnDate     = order['ReturnDate']
                    newOrder.status         = order['Status']
                    newOrder.deleted        = order['Deleted']
                    self.__orders.append(newOrder)
        return self.__orders

    def carDictWriter(self, order, file):
        Writer = csv.DictWriter(file, self.__fieldnames,restval = "", delimiter=",")
        Writer.writerow({'ID'                 : order.id,
                         'UserID'             : order.userId,
                         'CarCategory'        : order.carCategory,
                         'CarID'              : order.carId,
                         'Payment Method'     : order.payMethod,
                         'PickUpDate'         : order.pickUpDate,
                         'ReturnDate'         : order.returnDate,
                         'Status'             : order.status,
                         'Deleted'            : order.deleted})


    def getOrder(self, id):
        with open("./data/orders.csv", "r") as orderData:
            orderDict = csv.DictReader(orderData)
            for order in orderDict: 
                newOrder = Order()
                newOrder.id             = order['ID']
                newOrder.userId         = order['UserId']
                newOrder.carCategory    = order['CarCategory']
                newOrder.carId          = order['CarId']
                newOrder.payMethod      = order['Payment Method']
                newOrder.pickUpDate     = order['PickUpDate']
                newOrder.returnDate     = order['ReturnDate']
                newOrder.status         = order['Status']
                newOrder.deleted        = order['Deleted']
                return newOrder
