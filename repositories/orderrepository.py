from models.order import Order

class OrdersRepository:
    
    def __init__(self):
        self._orders = []


    def addOrder(self, order):
        with open("./data/orders.txt", "a+") as ordersFile:
            ordersFile.write("{},{},{},{},{},{},{},\n".format(order._id, order._userId, order._carCategory,\
        order._carId, order._payMethod, order._status, order._deleted))

                
    def getOrder(self):
        if self._orders == []:
            with open("./data/orders.txt", "r") as ordersFile:
                for line in ordersFile.readlines(): 
                    id, userId, carCatagory,carId, payMethod, status, deleted = line.split(",")
                    newOrder = Order(id, userId, carCatagory, carId, payMethod, status, deleted)
                    self._orders.append(newOrder)
        return self._orders

    #def updateOrder(self, order):

def addOrder(self, Order):
     with open("./data/orders.txt", "a+") as ordersFile:
        ordersFile.write("{},{},{},{},{},{},\n".format(Order._id, Order._userid, Order._carCategory,\
    Order._carId, Order._payMethod, Order._status,))

