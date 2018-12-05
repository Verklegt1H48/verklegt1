from models.car import Car

class CarRepository:

    def __init__(self):
        self.__car = []

    def addCar(self, car):
        with open("./data/cars.txt", "a+") as cars_file:
            category = car._category
            manufacturer = car._manufacturer
            model = car._model
            year = car._year
            milage = car._milage
            seats = car._seats
            transmission = car._transmission
            extras = car._extras
            id = car._id
            available = car._available
            cars_file.write("{},{},{},{},{},{},{},{},{},{}\n".format(category, manufacturer,
            model, year, milage, seats, transmission, extras, id, available))

    def getCar(self):
        if self.__car == []:
            with open("./data/cars.txt","r") as car_file:
                for line in car_file.readlines():
                    category, manufacturer, model, year, milage, seats, transmission, id = line.strip().split(",")
                    new_car = Car(category, manufacturer, model, year, milage, seats, transmission, id)
                    self.__car.append(new_car)
                return self.__car
   # def getCarList(self):

       # self._category = ""
       # self._manufacturer = ""
       # self._model = ""
       # self._year = 0
       # self._milage = 0
       # self._seats = 0
       # self._transmission = ""
       # self._extras = []
       # self._id = 0
       # self._deleted = False
       # self._rentHistory = []
       # self._available = True