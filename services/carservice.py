from repositories.carrepository import CarRepository

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()

    def addCar(self, car):
        #if self.isValidCar(car):
        self.__carRepo.addCar(car)
    
    
    def getCarList(self):
        return self.__car_repo.getCars()
 
   # def get_car_category(car, category):
    def getAndSortAvailableCars(self, attribute):
        allCars = self.getCars()
        availableCars = []
        for cars in allCars:
            if cars.deleted == False:
                availableCars.append(cars)
        
        return availableCars.sorted(availableCars, key = lambda availableCars: cars.category)
