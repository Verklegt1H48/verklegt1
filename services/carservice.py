from repositories.carrepository import CarRepository
from operator import attrgetter, methodcaller
from models.car import Car
class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()

    def addCar(self):
        newCar = Car()
        newCar.category =     input("Category: ")
        newCar.manufacturer = input("Manufacturer: ")
        newCar.model =        input("Model: ")
        newCar.year =         input("Year: ")
        newCar.mileage =       input("Mileage: ")
        newCar.seats =        input("Seats: ")
        newCar.transmission = input("Transmission: ")
        newCar.extras =       input("Extras: ")
        newCar.id =           len(self.__carRepo.__cars)
        newCar.price =        input("Price: ")
        self.__carRepo.addCar(newCar)
        
    
    def isValidCar(self, car):
        # ToDo
        # ToDo
        return True
    
    def getCarList(self):
        return self.__carRepo.getCarList()
 
    def getAndSortAvailableCars(self, attribute):
        allCars = self.getCarList()
        availableCars = []
        for cars in allCars:
            if cars.deleted == False:
                availableCars.append(cars)
        return sorted(availableCars, key=attrgetter(attribute))

    def getAvailableCarsByCategory(self, category):
        allCars = self.getCarList()
        availableCars = []
        for cars in allCars:
            if cars.deleted == False and cars.category == category:
                availableCars.append(cars)
        return availableCars[0]

