from models.car import Car
import csv

class CarRepository:

    def __init__(self):
        self.__cars = []

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
