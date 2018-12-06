from repositories.orderrepository import OrderRepository
from services.carservice import CarService
from models.order import Order
from operator import attrgetter, methodcaller

class OrderService:
    def __init__(self):
        self.__orderRepo = OrderRepository()
        self.__carService = CarService()

    def addOrder(self, order):
        newOrder = Order()
        newOrder.id =          len(self.getOrderList)
        newOrder.userId =      input("User ID: ")
        newOrder.carCategory = input("Car category: ")
        newOrder.payMethod =   input("Payment Method: ")
        newOrder.pickupDate =  input("Pickup date (dd/mm/yy): ")
        newOrder.returnDate =  input("Return date (dd/mm/yy): ")
        newOrder.status =      0
        newOrder.deleted =     0
        newOrder.carId =       self.__carService.getAvailableCarsByCategory(newOrder.carCategory).__id

        self.__orderRepo.addOrder(newOrder)

    def getOrderList(self):
        return self.__orderRepo.getOrderList()
 
    
    def getOrdersByStatus(self, status):
        allOrders = self.getOrderList()
        Orders = []
        for orders in allOrders:
            if orders.status == status:
                Orders.append(orders)
        
        return Orders
        #sorted(Orders, key = attrgetter(attribute))

        
