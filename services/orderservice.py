from repositories.orderrepository import OrderRepository
from models.order import Order
from operator import itemgetter, attrgetter, methodcaller

class OrderService:
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def addOrder(self, order):
        newOrder = Order()
        newOrder._id = len(self.getOrderList)
        newOrder._userId =      input("User ID: ")
        newOrder._carCategory = input("Car category: ")
        newOrder._carId =       input("Car ID: ")
        newOrder._payMethod =   input("Payment Method: ")
        newOrder._status =      1
        newOrder._deleted =     0

        self.__orderRepo.addOrder(newOrder)

    def getOrderList(self):
        return self.__orderRepo.getOrderList()
 
    
    def getAndSortAvailableCars(self, status, attribute):
        allOrders = self.getOrderList()
        Orders = []
        for orders in allOrders:
            if orders.deleted == status:
                Orders.append(orders)
        
        return sorted(Orders, key = attrgetter(attribute))

   # def get_car_category(car, category):
        
