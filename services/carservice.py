from repositories.carrepository import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def addCar(self, car):
        #if self.isValidCar(car):
        self.__car_repo.addCar(car)
    
    def isValidCar(self, car):
        # ToDo
        # ToDo
        return True
    
    def getCarList(self):
        return self.__car_repo.getCarList()
 


   # def get_car_category(car, category):
        
