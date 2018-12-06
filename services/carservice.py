from repositories.carrepository import CarRepository
from operator import itemgetter, attrgetter, methodcaller
class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()

    def addCar(self, car):
        #if self.isValidCar(car):
        self.__carRepo.addCar(car)
    
    
    def getCarList(self):
        return self.__carRepo.getCars()
 
   # def get_car_category(car, category):
    def getAndSortAvailableCars(self, attribute):
        allCars = self.getCarList()
        availableCars = []
        for cars in allCars:
            if cars.deleted == False:
                availableCars.append(cars)
        
        return sorted(availableCars, key=attrgetter(attribute))
