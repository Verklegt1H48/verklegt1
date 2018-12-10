from repositories.orderrepository import OrderRepository
from services.carservice import CarService
from models.order import Order
from helperfunctions.helpers import clearScreen
from operator import attrgetter, methodcaller
import sys

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
        newOrder.pickUpDate =  input("Pickup date (dd/mm/yy): ")
        newOrder.returnDate =  input("Return date (dd/mm/yy): ")
        self.__orders.append(newOrder)
        self.__orderRepo.addOrder(newOrder)

    def getOrderList(self):
        return self.__orders
    
    def getCategory(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Small ") 
            print("2. Confirmed orders") 
            print("3. Unconfirmed orders")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1":
                self.__orderService.addOrder()
                action = ""
            elif action == "2":
                self.printOrderList(1)
                action = ""
            elif action == "3":
                self.printOrderList(0)
                action = ""

    
    def getOrdersByStatus(self, status):
        orders = []
        for order in self.__orders:
            if order.status == status and order.deleted != 1:
                orders.append(order)
        return orders

    
