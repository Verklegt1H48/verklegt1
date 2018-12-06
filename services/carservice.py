from repositories.carrepository import CarRepository
from operator import attrgetter, methodcaller
from models.car import Car
class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()

    def addCar(self):
        newCar = Car()
        newCar.__category =     input("Category: ")
        newCar.__manufacturer = input("Manufacturer: ")
        newCar.__model =        input("Model: ")
        newCar.__year =         input("Year: ")
        newCar.__milage =       input("Milage: ")
        newCar.__seats =        input("Seats: ")
        newCar.__transmission = input("Transmission: ")
        newCar.__extras =       input("Extras: ")
        newCar.__id =           input("Id: ")
        newCar.__price =        input("Price: ")
        self.__carRepo.addCar(newCar)
    
    
    def getCarList(self):
        return self.__carRepo.getCarList()
 
   # def get_car_category(car, category):
    def getAndSortAvailableCars(self, attribute):
        allCars = self.getCarList()
        availableCars = []
        for cars in allCars:
            if cars.deleted == False:
                availableCars.append(cars)
        
        return sorted(availableCars, key=attrgetter(attribute))
