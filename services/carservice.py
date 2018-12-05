from repositories.carrepository import CarRepository

class CarService:
    def __init__(self):
        self.__carrepo = CarRepository()

    def addCar(self, car):
        #if self.isValidCar(car):
        self.__carrepo.addCar(car)
    
    def isValidCar(self, car):
        #
        #
        return True
    
    def getCar(self):
        return self.__carrepo.getCars()
 
   # def get_car_category(car, category):
        
