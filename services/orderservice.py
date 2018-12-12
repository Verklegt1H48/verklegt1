from repositories.orderrepository import OrderRepository
from repositories.carrepository import CarRepository
from services.carservice import CarService
from models.order import Order
from datetime import datetime
from helperfunctions.helpers import clearScreen
from operator import attrgetter, methodcaller
import sys

class OrderService:

    def __init__(self):
        self.__orderRepo = OrderRepository()
        self.__carRepo = CarRepository()
        self.__carService = CarService()
        self.__orders = self.__orderRepo.getOrderList()
        self.__cars = self.__carRepo.getCarList()

    def addOrder(self, newOrder):
        newOrder.id =          len(self.__orders)
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

    def deleteOrder(self, orderID):
        for order in self.__orders:
            if order.id == int(orderID):
                order.deleted = 1
            self.__orderRepo.overwriteOrders(self.__orders)
    
    def assigneCarToOrder(self, theCar, theOrder):
        for order in self.__orders:
            if order.id == int(theOrder.id):
                theOrder.carId = theCar.id
        for car in self.__cars:
            if car.id == int(theCar.id):
                car.available = 0
        self.__carRepo.overwriteCars(self.__cars)
        self.__orderRepo.overwriteOrders(self.__orders)

    def confirmOrder(self, orderID):
        for order in self.__orders:
            if order.id == int(orderID) and order.carId != -1:
                order.status = 1
            self.__orderRepo.overwriteOrders(self.__orders)
    
    def getOrdersByStatus(self, status):
        orders = []
        for order in self.__orderRepo.getOrderList():
            if order.status == status and order.deleted != 1:
                orders.append(order)
        return orders

    def obtainPickupAndReturnDate(self):
        action = ""
        while action != "b":
            action = input("When will you pick up your car? (dd/mm/yy): ")
            if action == "b" :
                return "", "", ""
            elif action == "q" :
                exit(1)
            try:
                pickupCar = datetime.strptime(action, "%d/%m/%y")
                if (pickupCar - datetime.today()).days > 365:
                    clearScreen()
                    print("You can't order more than a year in advance")
                    raise Exception
                elif pickupCar > datetime.today():
                    break
                else:
                    clearScreen()
                    raise Exception
            except:
                clearScreen()
                print("Invalid date input")
        pickUpDate = action  
        action = ""
        while action != "b":
            action = input("When will you return the car? (dd/mm/yy): ")
            if action == "b" :
                return "", "", ""
            elif action == "q" :
                exit(1)
            try:
                returnCar = datetime.strptime(action, "%d/%m/%y")
                if (returnCar - pickupCar).days > 365:
                    clearScreen()
                    if pickupCar.day < 10:
                        dayString = "0" + str(pickupCar.day)
                    if pickupCar.month < 10:
                        monthString = "0" + str(pickupCar.month)
                    yearString = str(pickupCar.year - 2000)
                    print("When will you pick up your car? (dd/mm/yy): " + dayString + "/" + monthString + "/" + yearString)
                    print("You can't have the car for more than a year")
                    raise Exception
                elif returnCar > pickupCar:
                    break
                else:
                    raise Exception
            except:
                clearScreen()
                print("Invalid date input")
        returnDate = action
        daysToRent = returnCar - pickupCar
        return pickUpDate, returnDate, daysToRent

    def isValidPayMethod(self, PayMethod):
        if PayMethod in ("CREDIT", "DEBIT", "CASH"):
            return True
        else:
            return False

    
