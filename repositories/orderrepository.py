from models.order import Order
def __init__(self):
    self._orders = []


def addOrder(self, Order):
     with open("./data/orders.txt", "a+") as ordersFile:
        ordersFile.write("{},{},{},{},{},{},\n".format(Order._id, Order._userid, Order._carCategory,\
    Order._carId, Order._payMethod, Order._status,))

            
def getOrder(self):
    if self._users == []:
        with open("./data/orders.txt", "r") as ordersFile:
            for line in ordersFile.readlines():
                id, userid, carCatagory,\
                carId, peyMethod, status = line.split(",")
                newOrder = Order(id, userid, carCatagory,\
                carId, peyMethod, status)
                self._users_orders.append(newOrder)
            return self._orders