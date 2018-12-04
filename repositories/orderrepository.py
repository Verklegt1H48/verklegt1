#from models.order import Order
def __init__(self):
    self._orders = []


def addUser(self, Order):
     with open("./data/orders.txt", "a+") as ordersFile:
        ordersFile.write("{},{},{},{},{},{},\n".format(self._id, self._userid, self._carCategory,\
    self._carId, self._payMethod, self._status,))

            
def getUsers(self):
    if self._users == []:
        with open("./data/orders.txt", "r") as ordersFile:
            for line in ordersFile.readlines():
                id, userid, carCatagory,\
                carId, peyMethod, status = line.split(",")
                newOrder = Order(id, userid, carCatagory,\
                carId, peyMethod, status)
                self._users_orders.append(newOrder)
            return self._orders