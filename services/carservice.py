from repositories.carrepository import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def addCar(self, car):
        #if self.isValidCar(car):
        self.__car_repo.addCar(car)
    
    def isValidCar(self, car):
        #
        #
        return True
    
    def getCar(self):
        return self.__car_repo.getCar()
 
   # def get_car_category(car, category):
        
