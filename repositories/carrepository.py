from models.car import Car
import csv

class CarRepository:

    def __init__(self):
        self.__cars = []

    def addCar(self, car):
        with open("./data/cars.csv", "a+") as carData:
            fieldnames = ["ID","Category","Manufacturer","Model","Year","Mileage","Seats","Transmission","Extras","Rent History","Deleted","Available"]
            carDictWriter = csv.DictWriter(carData, fieldnames, restval="")
            carDictWriter.writerow({'ID'           : car.id,
                                    'Category'     : car.category,
                                    'Manufacturer' : car.manufacturer,
                                    'Model'        : car.model,
                                    'Year'         : car.year,
                                    'Mileage'      : car.mileage,
                                    'Seats'        : car.seats,
                                    'Transmission' : car.transmission,
                                    'Extras'       : car.extras,
                                    'Deleted'      : car.deleted,
                                    'Rent History' : car.rentHistory,
                                    'Available'    : car.available})

    def getCarList(self):
        if self.__cars == []:
            with open("./data/cars.csv", 'r') as carData:
                carDict = csv.DictReader(carData)
                for car in carDict:
                    if car['Deleted'] == '1':
                        continue
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

    def getCar(self, id):
        with open("./data/cars.csv", 'r') as carData:
            carDict = csv.DictReader(carData)
            for car in carDict:
                if id == car['ID']:
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
                    self.__car = newCar
                    return self.__car
        return 0 #Returnar 0 til að byrja með