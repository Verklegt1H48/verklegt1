from repositories.carrepository import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def addCar(self, car):
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
        self.__car_repo.addCar(car)
    
    
    def getCarList(self):
        return self.__car_repo.getCarList()
 


   # def get_car_category(car, category):
        
