from repositories.carrepository import CarRepository
from repositories.orderrepository import OrderRepository
from operator import attrgetter, methodcaller
from models.car import Car
from datetime import date, timedelta, datetime


class CarService:

    def __init__(self):
        self.__carRepo = CarRepository()
        self.__orderRepo = OrderRepository()
        self.__cars = self.__carRepo.getCarList()
        self.__orders = self.__orderRepo.getOrderList()

    def addCar(self, newCar):
        newCar.id = len(self.__cars)
        self.__cars.append(newCar)
        self.__carRepo.addCar(newCar)

    def deleteCar(self, carID):
        success = False
        for car in self.__cars:
            if car.id == int(carID):
                car.deleted = 1
                success = True
        if success:
            self.__carRepo.overwriteCars(self.__cars)
        return success

    def makeCarAvailable(self, carID, mileage):
        success = False
        for car in self.__cars:
            if car.id == int(carID) and car.available == 0:
                car.available = 1
                car.mileage = mileage
                success = True
        if success:
            self.__carRepo.overwriteCars(self.__cars)
        return success

    def getCarList(self):
        return self.__cars

    def getAndSortAvailableCars(self, attribute):
        sortedCars = []
        if attribute == "available":
            for car in self.__cars:
                if not car.deleted and car.available:
                    sortedCars.append(car)
        else:
            for car in self.__cars:
                if not car.deleted:
                    sortedCars.append(car)
        return sorted(sortedCars, key=attrgetter(attribute))

    def getAvailableCarsByCategory(self, category):
        availableCars = []
        for car in self.__cars:
            if car.deleted == 0 and car.category == category and car.available == 1:
                availableCars.append(car)
        return availableCars

    def getFirstAvailableCarByCategory(self, category):
        for car in self.__cars:
            if car.deleted == 0 and car.category == category and  car.available == 1:
                return car

    def getCarOrders(self, id):
        carhistory = []
        for order in self.__orders:
            if order.carId == id:
                carhistory.append(order)
        return carhistory

    def getCarById(self, carID):
        for car in self.__cars:
            if car.id == int(carID) and car.available == 0:
                return car
        return ""

    def isValidCarId(self, id):
        cars = self.__cars
        for car in cars:
            if str(car.id) == str(id):
                return True
        return False

    def isValidCategory(self, category):
        if category in ("A", "B", "C", "D"):
            return True
        else:
            return False

    def isValidManufacturer(self, manufacturer):
        if (0 < len(manufacturer) <= 15) and all(x.isalnum() or x.isspace() for x in manufacturer):
            return True
        else:
            return False

    def isValidModel(self, model):
        return self.isValidManufacturer(model)

    def isValidYear(self, year):
        if year.isdecimal() and (1900 <= int(year) <datetime.today().year + 2):
            return True
        else:
            return False

    def isValidMileage(self, mileage, car = None):
        if car == None:
            car = Car()
            car.mileage = "0"
        if mileage.isdecimal() and (0 <= int(mileage) < 1000000) and int(car.mileage) < int(mileage):
            return True
        else:
            return False

    def isValidSeats(self, seats):
        if seats.isdecimal() and (0 < int(seats) <= 10):
            return True
        else:
            return False

    def isValidTransmission(self, transmission):
        if transmission in ("Manual", "Automatic"):
            return True
        else:
            return False

    def isValidExtras(self, extras):
        if (0 < len(extras) < 40):
            return True
        else:
            return False

    def isAvailableCar(self, carID):
        for car in self.__cars:
            if str(car.id) == str(carID) and str(car.available) == "1":
                return True
        return False
