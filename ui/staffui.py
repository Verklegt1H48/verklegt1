from models.car import Car
from models.order import Order
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
                clearScreen()
                counter = 1
                printHeader("carSelect")
                cars = self.__carService.getCarList()
                action = ""
                for car in cars:
                    print("{}{}".format(counter,car ))
                    counter += 1
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
                clearScreen()
                users = self.__userService.getUserList()
                action = ""
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
                newOrder = Order()
                newOrder.userId      = input("User ID: ")
                newOrder.carCategory = input("Car Category: ")
                car = self.carSelectionByCategory(newOrder.carCategory)
                newOrder.carId       = car.id
                newOrder.payMethod  = input("Payment Method: ")
                newOrder.pickUpDate, newOrder.returnDate, draslGildi = self.__orderService.obtainPickupAndReturnDate()
                self.__orderService.addOrder(newOrder)
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

            if orderToChange.carId == -1:
                print("This order has not been assigned a car\n")

            else :
                print("This order was assigned a car with ID: " + str(orderToChange.carId)+ "\n")

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
                self.__orderService.deleteOrder(orderToChange.id)
                action = "b"
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
        self.getValidCategory(newCar, self.__carService)
        self.getValidManufacturer(newCar, self.__carService)
        self.getValidModel(newCar, self.__carService)
        self.getValidYear(newCar, self.__carService)
        self.getValidMileage(newCar, self.__carService)
        self.getValidSeats(newCar, self.__carService)
        self.getValidTransmission(newCar, self.__carService)
        self.getValidExtras(newCar, self.__carService)
        self.getValidPrice(newCar, self.__carService)
        self.__carService.addCar(newCar)
        input("You have successfully added a new car. Please press Enter to continue")

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

    def getValidCategory(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            category = input("Category: ").upper()
            if service.isValidCategory(category):
                car.category = category
                isValid = True
            else:
                print("Invalid input. Category must be \"A\", \"B\", \"C\" or \"D\"")
                input("Please press enter to try again")

    def getValidManufacturer(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            manufacturer = input("Manufacturer: ")
            if service.isValidManufacturer(manufacturer):
                car.manufacturer = manufacturer.capitalize()
                isValid = True
            else:
                print("Invalid input. Manufacturer must be less than 15 letters")
                input("Please press enter to try again")

    def getValidModel(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            model = input("Model: ")
            if service.isValidModel(model):
                car.model = model.capitalize()
                isValid = True
            else:
                print("Invalid input. Model must be less than 15 letters")
                input("Please press enter to try again")

    def getValidYear(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            year = input("Year: ")
            if service.isValidYear(year):
                car.year = year
                isValid = True
            else:
                print("Invalid input. Year must be a valid year between 1900 and {}".format(datetime.today().year + 1))
                input("Please press enter to try again")

    def getValidMileage(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            mileage = input("Mileage: ")
            if service.isValidMileage(mileage):
                car.mileage = mileage
                isValid = True
            else:
                print("Invalid input. Mileage must be an integer between 0 and 100000")
                input("Please press enter to try again")

    def getValidSeats(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            seats = input("Seats: ")
            if service.isValidSeats(seats):
                car.seats = seats
                isValid = True
            else:
                print("Invalid input. Number of seats must be between 1 and 10")
                input("Please press enter to try again")

    def getValidTransmission(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            transmission = input("Transmission: ").capitalize()
            if service.isValidTransmission(transmission):
                car.transmission = transmission.capitalize()
                isValid = True
            else:
                print("Invalid input. Transmission must be either \"Manual\" or \"Automatic\"")
                input("Please press enter to try again")

    def getValidExtras(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            print("Input all extras seperated with a comma")
            print("If there are no extras input \"None\"")
            extras = input("Extras: ")
            if service.isValidExtras(extras):
                car.extras = extras
                isValid = True
            else:
                print("Invalid input. Extras must be less than 40 letters long")
                input("Please press enter to try again")

    def getValidPrice(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            price = input("Price: ")
            if service.isValidPrice(price):
                car.price = price
                isValid = True
            else:
                print("Invalid input. Price must be \"5000\", \"10000\", \"15000\" or \"20000\"")
                input("Please press enter to try again")
                