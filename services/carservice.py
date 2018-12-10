from repositories.carrepository import CarRepository
from operator import attrgetter, methodcaller
from models.car import Car


class CarService:

    def __init__(self):
        self.__carRepo = CarRepository()
        self.__cars = self.__carRepo.getCarList()

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
            if car.deleted is False:
                availableCars.append(car)
        return sorted(availableCars, key=attrgetter(attribute))

    def getAvailableCarsByCategory(self, category):
        availableCars = []
        for car in self.__cars:
            if car.deleted is False and car.category == category:
                availableCars.append(car)
        return availableCars

    def getFirstAvailableCarByCategory(self, category):
        for car in self.__cars:
            if car.deleted is False and car.category == category:
                return car
