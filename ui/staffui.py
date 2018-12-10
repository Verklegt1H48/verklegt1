from models.car import Car
from services.carservice import CarService
from services.orderservice import OrderService
from models.user import User
from datetime import datetime
from helperfunctions.helpers import clearScreen
import sys
#from ui.mainui import MainUI

class StaffUI:

    def __init__(self):
        #self.__mainui = MainUI()
        self.__carService = CarService()
        self.__orderService = OrderService()

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
                self.__carService.addCar()
            elif action == "3":
                cars = self.__carService.getCarList()
                for car in cars:
                    print(car)
                input("")

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
            elif action == "2" :
                self.staffCustomerMenu()
            elif action == "3" :
                self.orderMenu()

    def staffCustomerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("\n\n1. Add a customer")
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
                self.__carService.addCar()
            elif action == "3":
                car = self.__carService.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.staffCarMenu()

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
            elif action == "2":
                unconf = self.__orderService.getOrdersByStatus(1)
                print(unconf)
                action = ""
            elif action == "3":
                conf = self.__orderService.getOrdersByStatus(0)
                print(conf)
                action = ""
                

