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
        newCar.milage =       input("Milage: ")
        newCar.seats =        input("Seats: ")
        newCar.transmission = input("Transmission: ")
        newCar.extras =       input("Extras: ")
        #newCar_id =           input("Id: ")
        newCar.id =           len(self.getCarList())
        newCar.price =        input("Price: ")
        print(newCar)
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
        
        return sorted(availableCars, key = attrgetter(attribute))
