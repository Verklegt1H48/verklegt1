from models.car import Car
from services.carservice import CarService
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__car_service = CarService()
        self._action = ""
    def mainMenu(self):

        while(self._action != "q"):
            print("Welcome to the best car rental in the world!")
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("Press q to quit any time")
            self._action = input("Choose an option: ")



    def addCarMenu(self):
            print("1. Add a car")
            print("2. List all car")
            print("Press q to quit")
            newCar = Car()
            self._action = input("Choose an option").lower()

            if self._action == "1":
                newCar._category = input("Category: ")
                newCar._manufacturer = input("Manufacturer: ")
                newCar._model = input("Model: ")
                newCar._year = input("Year: ")
                newCar._milage = input("Milage: ")
                newCar._seats = input("Seats: ")
                newCar._transmission = input("Transmission: ")
                newCar._extras = input("Extras: ")
                newCar._id = input("Id: ")
                self.__car_service.addCar(newCar)

            elif self._action == "2":
                car = self.__car_service.getCar()
                print(car)        