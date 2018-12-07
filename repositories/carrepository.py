from models.car import Car
import csv
import os.path

class CarRepository:

    #Initialization of CarRepository
    def __init__(self):
        self.__cars = []
        self.__fieldnames = ["ID","Category","Manufacturer","Model","Year","Mileage","Seats","Transmission","Extras","Rent History","Deleted","Available","Price"]

    #Function to write car objects into a file
    def carDictWriter(self, car, file):
        Writer = csv.DictWriter(file, self.__fieldnames,restval = "", delimiter=",")
        Writer.writerow({'ID'           : car.id,
                         'Category'     : car.category,
                         'Manufacturer' : car.manufacturer,
                         'Model'        : car.model,
                         'Year'         : car.year,
                         'Mileage'      : car.mileage,
                         'Seats'        : car.seats,
                         'Transmission' : car.transmission,
                         'Extras'       : str(car.extras).strip("[']").replace("', '",","),
                         'Deleted'      : car.deleted,
                         'Rent History' : str(car.rentHistory).strip("[']").replace("', '",","),
                         'Available'    : car.available,
                         'Price'        : car.price})

    #Function to open cars.csv and add an instance of car to the end of the file
    def addCar(self, car):
        if not os.path.isfile('./data/cars.csv'):
            with open("./data/cars.csv", "w+", newline = '') as carData:
                csv.writer(carData).writerow(self.__fieldnames)
                self.carDictWriter(car, carData)
        else:
            with open("./data/cars.csv", "a+", newline = '') as carData:
                self.carDictWriter(car, carData)

    #Function to open cars.csv and overwrite the whole list with an updated list of cars.
    def overwriteCars(self, cars):
        with open("./data/cars.csv", "w+", newline = '') as carData:
            csv.writer(carData).writerow(self.__fieldnames)
            for car in cars:
                self.carDictWriter(car, carData)

    #Function to open cars.csv with DictReader and make a list of cars from the dictionary
    def getCarList(self):
        if self.__cars == []:
            try:
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
                        newCar.deleted      = car['Deleted']
                        newCar.rentHistory  = car['Rent History'].strip("").split(",")
                        newCar.available    = car['Available']
                        newCar.price        = car['Price']

                        for extra in car['Extras'].split(","):
                            newCar.extras.append(extra)

                        self.__cars.append(newCar)
            except FileNotFoundError:
                pass
        return self.__cars
