from models.order import Order
import csv

class OrderRepository:
    
    def __init__(self):
        self._orders = []


    def addOrder(self, order):
        with open("./data/orders.csv", "a+") as ordersFile:
            ordersFile.write("{},{},{},{},{},{},{},\n".format(order._id, order._userId, order._carCategory,\
        order._carId, order._payMethod, order._status, order._deleted))

                
    def getOrderList(self):
        if self._orders == []:
            with open("./data/orders.csv", "r") as orderData:
                orderDict = csv.DictReader(orderData)
                for order in orderDict: 
                    newOrder = Order()
                    newOrder.id             = order['id']
                    newOrder.userId         = order['userId']
                    newOrder.carCategory    = order['carCategory']
                    newOrder.carId          = order['carId']
                    newOrder.payMethod      = order['payMethod']
                    newOrder.status         = order['status']
                    newOrder.deleted        = order['deleted']
                    self._orders.append(newOrder)
        return self._orders

    def getOrder(self, id):
        with open("./data/orders.csv", "r") as orderData:
            orderDict = csv.DictReader(orderData)
            for order in orderDict: 
                newOrder = Order()
                newOrder.id             = order['id']
                newOrder.userId         = order['userId']
                newOrder.carCategory    = order['carCategory']
                newOrder.carId          = order['carId']
                newOrder.payMethod      = order['payMethod']
                newOrder.status         = order['status']
                newOrder.deleted        = order['deleted']
                return newOrder
