from models.car import Car
from services.carservice import CarService
from services.orderservice import OrderService
from services.userservice import UserService
from models.user import User
from datetime import datetime
from helperfunctions.helpers import clearScreen
from ui.headers import printHeader
from ui.customerui import CustomerUI
import sys
import getpass
#from ui.mainui import MainUI

class StaffUI:

    def __init__(self):
        #self.__mainui = MainUI()
        self.__carService = CarService()
        self.__orderService = OrderService()
        self.__userService = UserService()

    def staffMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Car management")
            print("2. Customer management") 
            print("3. Orders")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1" :
                self.staffCarMenu()
                action = ""
            elif action == "2" :
                self.staffCustomerMenu()
                action = ""
            elif action == "3" :
                self.orderMenu()
                action = ""

    def staffCarMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                sys.exit()
            elif action == "1":
                self.addCar()
                action = ""
            elif action == "2":
                self.removeCar()
                action = ""
            elif action == "3":
                cars = self.__carService.getCarList()
                for car in cars:
                    print(car)
                input("")

    def staffCustomerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Add a customer")
            print("2. Remove a customer")
            print("3. List all customers")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1":
                self.addUser()
            elif action == "3":
                car = self.__carService.getCarList()
                print(car)

    def orderMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. New order") 
            print("2. Confirmed orders") 
            print("3. Unconfirmed orders")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1":
                self.__orderService.addOrder()
                action = ""
            elif action == "2":
                self.printOrderList(1)
                action = ""
            elif action == "3":
                self.printOrderList(0)
                action = ""

    def printOrderList(self, status):
        action = ""
        while action != "b":
            clearScreen()
            orderList = self.__orderService.getOrdersByStatus(status)
            counter = 1
            printHeader("orderSelect")
            for order in orderList:
                print("{}{}".format(counter,order ))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            print("Press b to return to the previous page")
            print("Press q to quit")
            action = input("Please select the order you wish to change: ").lower()
            if action == "q" :
                exit(1)
            elif action.isdecimal() == False:
                pass
            elif int(action) >= counter:
                pass
            elif int(action) <= 0:
                pass
            else:
                self.inputOrderInfo(orderList[int(action) - 1])
                action = ""
                del orderList
               
    def inputOrderInfo(self, carToOrder):
        clearScreen()
        print("You chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
        print("Current price is " + carToOrder.price + " isk per day")
        #currPrice = ""
        #currPrice = self.addInsurance(carToOrder)
        #if(currPrice != ""):
        #    daysToRent = self.obtainPickupAndReturnDate()
        #    if(daysToRent != ""):
        #        finalPrice = int(daysToRent.days) * int(currPrice)
        #        print("Your final price is " + str(finalPrice) + " isk")
        
    def addCar(self):
        newCar = Car()
        newCar.id            = len(self.__carService.__cars)
        newCar.category      = input("Category: ")
        newCar.manufacturer  = input("Manufacturer: ")
        newCar.model         = input("Model: ")
        newCar.year          = input("Year: ")
        newCar.mileage       = input("Mileage: ")
        newCar.seats         = input("Seats: ")
        newCar.transmission  = input("Transmission: ")
        newCar.extras        = input("Extras: ")
        newCar.price         = input("Price: ")

    def addUser(self):
        CustomerUI.createAccount(self, self.__userService)

    def removeCar(self):
        clearScreen()
        choice = ""
        id = input("Enter the ID of the car you want to delete: ")
        if id == "q":
            sys.exit()
        if id == "b":
            return
        choice = input("Are you sure you want to delete car with ID: \"{}\"? y/n: ".format(id)).lower()
        while choice not in ("b","y","n","q"):
            choice = input("Please input \"y\" or \"n\"!: ").lower()
        clearScreen()
        if choice == "y":
            if self.__carService.deleteCar(id):
                print("You have deleted the car with ID: \"{}\"".format(id))
                input("Press enter to continue")
            else:
                print("No car with ID: \"{}\" exists. Please try again".format(id))
                input("Press enter to continue")
        if choice == "n":
            print("You aborted the deletion of the car with ID: \"{}\"".format(id))
            input("Press enter to continue")
        if choice == "q":
            sys.exit()
