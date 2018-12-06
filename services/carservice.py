from repositories.carrepository import CarRepository
from operator import itemgetter, attrgetter, methodcaller
from models.car import Car
class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()

    def addCar(self):
        newCar = Car()
        newCar._category =     input("Category: ")
        newCar._manufacturer = input("Manufacturer: ")
        newCar._model =        input("Model: ")
        newCar._year =         input("Year: ")
        newCar._milage =       input("Milage: ")
        newCar._seats =        input("Seats: ")
        newCar._transmission = input("Transmission: ")
        newCar._extras =       input("Extras: ")
        newCar._id =           input("Id: ")
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
