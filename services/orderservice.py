from repositories.orderrepository import OrderRepository
from services.carservice import CarService
from models.order import Order
from operator import attrgetter, methodcaller

class OrderService:

    def __init__(self):
        self.__orderRepo = OrderRepository()
        self.__carService = CarService()
        self.__orders = self.__orderRepo.getOrderList()

    def addOrder(self):
        newOrder = Order()
        newOrder.id =          len(self.__orders)
        newOrder.userId =      input("User ID: ")
        newOrder.carCategory = input("Car category: ")
        newOrder.payMethod =   input("Payment Method: ")
        newOrder.pickupDate =  input("Pickup date (dd/mm/yy): ")
        newOrder.returnDate =  input("Return date (dd/mm/yy): ")
        newOrder.status =      0
        newOrder.deleted =     0
        self.__orders.append(newOrder)
        self.__orderRepo.addOrder(newOrder)

    def getOrderList(self):
        return self.__orders

    
    def getOrdersByStatus(self, status):
        orders = []
        for order in self.__orders:
            if order.status == status:
                orders.append(order)
        return orders
