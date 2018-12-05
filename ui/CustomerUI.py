from models.car import Car
from services.carservice import CarService
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__carservice = CarService()
        self._action = ""
    def mainMenu(self):

        print("Welcome to the best car rental in the world!")
        print("1. See available cars")
        print("2. Log in as customer")
        print("3. Log in as staff")
        print("Press q to quit any time")
        self._action = input("Choose an option: ")

        if self._action == "q" :
            return

        if self._action == "1":
            print("ekkert")

        if self._action == "2":
            print("ekkert")
        
        if self._action == "3":
            print("ekkert")
        


    def carMenu(self):
            print("1. Add a car")
            print("2. Remove a car")
            print("3. List all car")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self._action = input("Choose an option").lower()

            if self._action == "b" :
                self.staffMenu()

            if self._action == "q" :
                return

            if self._action == "1":
                newCar = Car()
                newCar._category = input("Category: ")
                newCar._manufacturer = input("Manufacturer: ")
                newCar._model = input("Model: ")
                newCar._year = input("Year: ")
                newCar._milage = input("Milage: ")
                newCar._seats = input("Seats: ")
                newCar._transmission = input("Transmission: ")
                newCar._extras = input("Extras: ")
                newCar._id = input("Id: ")
                self.__carservice.addCar(newCar)

            elif self._action == "3":
                car = self.__carservice.getCar()
                print(car)

    def staffMenu(self):
        print("1. Car management")
        print("2. Customer management") 
        print("3. Orders")
        print("Press b to return to the previous page")
        print("Press q to quit")
        self._action = input("Choose an option").lower()

        if self._action == "b" :
            self.mainMenu()
        if self._action == "q" :
            return
        if self._action == "1" :
            print("ekkert")
        