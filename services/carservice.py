from repositories.carrepository import CarRepository
from repositories.orderrepository import OrderRepository
from operator import attrgetter, methodcaller
from models.car import Car
from datetime import date, timedelta, datetime


class CarService:

    def __init__(self):
        self.__carRepo = CarRepository()
        self.__orderRepo = OrderRepository()
        self.__cars = self.__carRepo.getCarList()
        self.__orders = self.__orderRepo.getOrderList()

    def addCar(self):
        newCar = Car()
        newCar.id            = len(self.__cars)
        newCar.category      = input("Category: ")
        newCar.manufacturer  = input("Manufacturer: ")
        newCar.model         = input("Model: ")
        newCar.year          = input("Year: ")
        newCar.mileage       = input("Mileage: ")
        newCar.seats         = input("Seats: ")
        newCar.transmission  = input("Transmission: ")
        newCar.extras        = input("Extras: ")
        newCar.price         = input("Price: ")
        self.__cars.append(newCar)
        self.__carRepo.addCar(newCar)
        
    def isValidCar(self, car):
        # ToDo
        # ToDo
        return True
    
    def getCarList(self):
        return self.__carRepo.getCarList()
 
    def getAndSortAvailableCars(self, attribute):
        availableCars = []
        for car in self.__cars:
            if car.deleted:
                availableCars.append(car)
        return sorted(availableCars, key=attrgetter(attribute))

    def getAvailableCarsByCategory(self, category):
        availableCars = []
        for car in self.__cars:
            if car.deleted and car.category == category:
                availableCars.append(car)
        return availableCars

    def getFirstAvailableCarByCategory(self, category):
        for car in self.__cars:
            if car.deleted and car.category == category:
                return car
    
    def getCarOrders(self, id):
        carhistory = []
        for order in self.__orders:
            if order.carId == id:
                carhistory.append(order)
        return carhistory
    
    def getCarHistory(self, id):
        orders = self.getCarOrders(id)
        history = []
        for order in orders:
            pickUpDate = order.pickUpDate
            returnDate = order.returnDate
            pickUpDate = datetime.strptime(pickUpDate, "%d/%m/%y")
            returnDate = datetime.strptime(returnDate, "%d/%m/%y")
            carHistory = returnDate - pickUpDate
            for i in range(carHistory.days + 1):
                date = pickUpDate + timedelta(i)
                history.append(datetime.strftime(date, "%d/%m/%y"))
        print(history)
        return history
            




