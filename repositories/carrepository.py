from models.car import Car
import csv

class CarRepository:

    def __init__(self):
        self.__cars = []

    def addCar(self, car):
        with open("./data/cars.txt", "a+") as cars_file:
            category = car.category()
            manufacturer = car.manufacturer()
            model = car.model()
            year = car.year()
            milage = car.milage()
            seats = car.seats()
            transmission = car.transmission()
            extras = car.extras()
            id = car.id()
            available = car.isAvailable()
            cars_file.write("{},{},{},{},{},{},{},{},{},{}\n".format(category, manufacturer,
            model, year, milage, seats, transmission, extras, id, available))

    def getCars(self):
        if self.__cars == []:
            with open("./data/cars.csv", 'r') as carData:
                carDict = csv.DictReader(carData)
                for car in carDict:
                    newCar = Car()
                    newCar.id           = car['ID']
                    newCar.category     = car['Category']
                    newCar.manufacturer = car['Manufacturer']
                    newCar.model        = car['Model']
                    newCar.year         = car['Year']
                    newCar.mileage      = car['Mileage']
                    newCar.seats        = car['Seats']
                    newCar.transmission = car['Transmission']
                    newCar.extras       = car['Extras']
                    newCar.deleted      = car['Deleted']
                    newCar.rentHistory  = car['Rent History']
                    newCar.available    = car['Available']
                    self.__cars.append(newCar)
        return self.__cars

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