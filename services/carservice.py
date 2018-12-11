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
    
    def getCarList(self):
        return self.__cars
 
    def getAndSortAvailableCars(self, attribute):
        availableCars = []
        for car in self.__cars:
            if not car.deleted:
                availableCars.append(car)
        return sorted(availableCars, key=attrgetter(attribute))

    def getAvailableCarsByCategory(self, category):
        availableCars = []
        for car in self.__cars:
            if car.deleted == 0 and car.category == category and car.available == 1 :
                availableCars.append(car)
        return availableCars

    def getFirstAvailableCarByCategory(self, category):
        for car in self.__cars:
            if car.deleted == 0 and car.category == category and  car.available == 1 :
                return car
    
    def getCarOrders(self, id):
        carhistory = []
        for order in self.__orders:
            if order.carId == id:
                carhistory.append(order)
        return carhistory
    
    #Hér er breytt strengjum í datetime til að reikna allar dagsetningar á milli tveggja datetime-a
    #Síðan er þeim breytt aftur í streng
    def getCarHistory(self, id):
        orders = self.getCarOrders(id)
        history = []
        for order in orders:
            pickUpDate = order.pickUpDate
            returnDate = order.returnDate
            pickUpDate = datetime.strptime(pickUpDate, "%d/%m/%y")
            returnDate = datetime.strptime(returnDate, "%d/%m/%y")
            carHistory = returnDate - pickUpDate
            for i in range(carHistory.days + 1):
                date = pickUpDate + timedelta(i)
                history.append(datetime.strftime(date, "%d/%m/%y"))
        print(history)
        return history

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
        if (1990):
            return True
        else:
            return False

    def isValidYear(self, year):
        if year.isdecimal() and (1900 <= int(year) <datetime.today().year + 2):
            return True
        else:
            return False

    def isValidMileage(self, mileage):
        if mileage.isdecimal() and (0 <= int(mileage) < 100000):
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
        if extras.isalnum() and (0 < len(extras) < 40):
            return True
        else:
            return False

    def isValidPrice(self, price):
        if price in ("5000", "10000", "15000", "20000"):
            return True
        else:
            return False
