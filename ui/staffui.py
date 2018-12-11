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
        self.__isLoggedIn = False
        self.__userName = ""

    def staffMenu(self):
        action = ""
        while action != "b": 
            clearScreen()
            print("Welcome " + self.__userName + "!") 
            print("1. Car management")
            print("2. User management") 
            print("3. Orders")
            print("Press b to sign out")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1" :
                action = ""
                self.staffCarMenu()
            elif action == "2" :
                action = ""
                self.staffCustomerMenu()
            elif action == "3" :
                action = ""
                self.orderMenu()

    def staffCarMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
           # print("4. List all unavaliable cars")
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
                action = ""
                clearScreen()
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
            print("4. Add a new staff member")
            print("Press b to return to the previous page")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q" :
                sys.exit()
            elif action == "1":
                action = ""
                clearScreen()
                self.addUser()
            #elif action == "2":
                #self.__userService.deleteUser()
                #action = ""
            elif action == "3":
                users = self.__userService.getUserList()
                action = ""
                clearScreen()
                for user in users:
                    print(user)
                input("Input any key to go back: ")
            elif action == "4":
                self.addStaffMember()
                action = ""
                clearScreen()

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
              
    def inputOrderInfo(self, orderToChange):
        pass
        action = ""
        while action != "b":
            clearScreen()
            if action != "":
                print("Invalid input, try again")
            print("You chose an order with ID: " + str(orderToChange.id))
            if orderToChange.status == 1:
                orderStatus = "Confirmed"
            else :
                orderStatus = "Unconfirmed"
            print("This order is " + orderStatus)
            if orderToChange.carId == -1:
                print("This order has not been assigned a car\n")
            if action != "":
                print("Invalid input, try again")
            else :
                print("This order was assigned a car with ID: " + str(orderToChange.carId))

            print("1. To delete order")

            print("2. To confirm order")
            if orderToChange.carId == -1:
                print("3. To assign a car to this order")
            print("Press b to return to the previous page")
            print("Press q to quit")
            action = input("Please select what you wish to change: ").lower()
            if action == "q":
                sys.exit()
            elif action == "1" :
                orderToChange.deleted = 1
            elif action == "2" :
                self.__orderService.confirmOrder(orderToChange.id)
                action = "b"
            elif action == "3" :
                self.carAssignment(orderToChange)
                action = "b"
                
    
    def carAssignment(self, order):
        car = self.__carService.getFirstAvailableCarByCategory(order.carCategory)
        if car == None:
                print("\n ***No car available in that category***\n")
                input("Press enter to go back")
                return
        print("\n Manufacturer: {} , {}\n Year: {}\n Mileage: {}\n Seats: {}\n Transmission: {}\n Extras: {}".format
        (car.manufacturer,str(car.model), str(car.year), str(car.mileage),str(car.seats),
        car.transmission,str(car.extras).strip("[']").replace("', '", ", ")) )

        action = ""
        while action != "b":
            action = input("Would you like to assign this car to the order Y/N: ").lower()
            if action == "q" :
                sys.exit()
            if action == "y" :
                self.__orderService.assigneCarToOrder(car,order)
            elif action == "n" :
                car = self.carSelectionByCategory(order.carCategory)
                self.__orderService.assigneCarToOrder(car,order)
            if action != "":
                print("Invalid input, try again")
            

    def carSelectionByCategory(self, category):
        action = ""
        while action != "b":
            clearScreen()
            carList = self.__carService.getAvailableCarsByCategory(category)
            counter = 1
            printHeader("carSelect")
            for car in carList:
                print("{:5}{}".format(counter,car))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            action = input("Please select the car you wish to book: ").lower()
            if action == "q" :
                exit(1)
            elif action.isdecimal() == False:
                pass
            elif int(action) >= counter:
                pass
            elif int(action) <= 0:
                pass
            else:
                return carList[int(action) - 1]

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

    def addStaffMember(self):
        clearScreen()
        employeeName = input("Enter employee name: ")
        employeeSocialNumber = input("Enter employee social security number: ")
        employeePin = input("Enter unique employee number: ")
        newUser = User(employeeName, employeeSocialNumber, 0, employeePin)
        self.__userService.addUser(newUser)


    def logInAsStaff(self):
        staffSocial = self.getStaffSocial()
        if staffSocial != "":
            self.getStaffPin(staffSocial)
            if self.__isLoggedIn:
                self.staffMenu()
        
    
    def getStaffSocial(self):
        action = ""
        clearScreen()
        while action != "b":
            action = input("Enter your social security number: ")
            selectedUser = self.__userService.getUserBySocial(action)
            if(action == "q"):
                exit(1)
            elif selectedUser == "Not found":
                clearScreen()
                print("Staff member not found!")
            else:
                if selectedUser.employee == "0":
                    return action
                else:
                    clearScreen()
                    print("Staff member not found!")
                    
        return ""

    def getStaffPin(self, staffSocial):
        action = ""
        while action != "b":
            clearScreen()
            if action != "":
                print("Invalid pin!")

            print("Enter your social security number: " + staffSocial)
            action = getpass.getpass("Enter your unique employee number: ")
            selectedUser = self.__userService.getUserBySocial(staffSocial)

            if(action == "q"):
                exit(1)
            elif selectedUser.pin == action:
                clearScreen()
                self.__userName = selectedUser.name
                self.__isLoggedIn = True
                return