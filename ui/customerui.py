from services.carservice import CarService
from services.userservice import UserService
from models.car import Car
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__carService = CarService()
        self.__userService = UserService()
        self.__action = ""
    def mainMenu(self):

        while(self.__action != "q"):
            print("Welcome to the best car rental in the world!")
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("Press q to quit any time")
            self.__action = input("Choose an option: ")
            if self.__action == "1":
                self.seeAvailableCars()
            elif self.__action == "2":
                print("")
            elif self.__action == "3":
                print("")

    def seeAvailableCars(self):
        while(self.__action != "q"): 
            print("How would you like to sort the car list?")
            print("1. By price")
            print("2. By availability")
            print("3. By type")
            print("4. By category")
            self.__action = input("Choose an option: ")
            if self.__action == "1":
                self.printCarList(4)
            elif self.__action == 2:
                self.printCarList(7)
            elif self.__action == 3:
                self.printCarList(3)
    
    def printCarList(self, attribute):
        carList = self.__carService.getAndSortAvailableCars(3)
        counter = 0
        for car in carList:
            print(counter + ". " + car)
            counter += 1


    def addCarMenu(self):
            print("1. Add a car")
            print("2. List all car")
            print("Press q to quit")
            newCar = Car()
            self._action = input("Choose an option: ").lower()

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
                self.__carService.addCar(newCar)

            elif self._action == "2":
                car = self.__carService.getCars()
                print(car)        