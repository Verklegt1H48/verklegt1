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
        newOrder.id = len(self.__orders)
        self.__orders.append(newOrder)
        self.__orderRepo.addOrder(newOrder)

    def getOrderList(self):
        return self.__orders

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

    def isValidPickUpDate(self, pickUpDate):
        try:
            pickupCar = datetime.strptime(pickUpDate, "%d/%m/%y")
        except:
            return "Invalid"
        if (pickupCar - datetime.today()).days > 365 :
            return "Year"
        elif datetime.today() > pickupCar:
            return "Past"
        else :
            return pickupCar

    def isValidReturnDate(self, returnDate, pickUpCar):
        try:
            returnCar = datetime.strptime(returnDate, "%d/%m/%y")
        except:
            return "Invalid"
        if (returnCar - pickUpCar).days > 365:
            return "Year"
        elif returnCar <= pickUpCar:
            return "Past"
        else : 
            return returnCar

    def calcPrice(self, pickUpDate, returnDate, currPrice):
        pickUpCar = datetime.strptime(pickUpDate, "%d/%m/%y")
        returnCar = datetime.strptime(returnDate, "%d/%m/%y")
        daysToRent = returnCar - pickUpCar
        finalPrice = int(daysToRent.days) * int(currPrice)
        return finalPrice


    def isValidPayMethod(self, PayMethod):
        if PayMethod in ("CREDIT", "DEBIT", "CASH"):
            return True
        else:
            return False

    
