from models.car import Car
from models.user import User
from models.order import Order
from services.userservice import UserService
from services.carservice import CarService
from services.orderservice import OrderService
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen
import getpass

class CustomerUI:
    
    def __init__(self):
        self.__userService = UserService()
        self.__carService = CarService()
        self.__orderService = OrderService()
        self.__isLoggedIn = False
        self.__currUser = User()

    def seeAvailableCars(self):
        action = ""
        while action != "b":
            clearScreen()
            if self.__isLoggedIn:
                print("Welcome " + self.__currUser.name + "!")
            print("Press q to quit and b to go back")
            print("How would you like to sort the car list?")
            print("1. By price category")
            print("2. By manufacturer")
            print("3. By availability")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                exit(1)
            elif action == "1":
                self.printCarList("price")
                action = ""
            elif action == "2":
                self.printCarList("manufacturer")
                action = ""
            elif action == "3":
                self.printCarList("available")
                action = ""
                
    
    def printCarList(self, attribute):
        action = ""
        while action != "b":
            clearScreen()
            carList = self.__carService.getAndSortAvailableCars(attribute)
            counter = 1
            printHeader("carSelect")
            for car in carList:
                print("{:5}{}".format(counter,car))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            if self.__isLoggedIn == True:
                action = input("Please select the car you wish to book: ").lower()
            else:
                print("You need to log in to book a car")
                action2 = input("Input 'login' to go to login screen: ")
                if action2 == "login":
                    self.customerMenu()
                else:
                    pass
           
            if action == "q" :
                exit(1)
            elif action.isdecimal() == False:
                pass
            elif int(action) >= counter:
                pass
            elif int(action) <= 0:
                pass
            else:
                carToOrder = carList[int(action) - 1]
                pickUpDate, returnDate = self.inputOrderInfo(carToOrder)
                newOrder = Order(self.__currUser.id, carToOrder.category, carToOrder.id, "*payment*", pickUpDate, returnDate)
                self.__orderService.addOrder(newOrder)
                newOrder = Order()
                action = ""
                del carList
               

    def inputOrderInfo(self, carToOrder):
        clearScreen()
        print("You chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
        print("Current price is " + str(carToOrder.price) + " isk per day")
        currPrice = ""
        currPrice = self.addInsurance(carToOrder)
        if(currPrice != ""):
            pickUpDate, returnDate, daysToRent = self.__orderService.obtainPickupAndReturnDate()
            if(daysToRent != ""):
                finalPrice = int(daysToRent.days) * int(currPrice)
                print("Your final price is " + str(finalPrice) + " isk")
                return pickUpDate, returnDate
            
    def addInsurance(self, carToOrder):
       
        action = ""
        while action != "b":
            clearScreen()
            print("Press q to quit and b to go back")  
            carInsurance = str(int(int(carToOrder.price) / 10))
            if action != "":
                print("Invalid input, try again")
            action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")
            
            if action == "q" :
                exit(1)
            elif action == "y":    
                totalPrice = str(int(carInsurance) + int(carToOrder.price))
                print("Your total price per day is " + totalPrice + " isk")
                return totalPrice
            elif action == "n":
                print("Your total price per day is " + carToOrder.price + " isk")
                return carToOrder.price
            else:
                pass
        return ""
                    
    def customerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("1. Log in")
            print("2. Sign up")
            print("Press q to quit and b to go back") 
            if action != "":
                print("Invalid input, try again")
            action = input("Choose an option: ").lower()
            if action == "q" :
                exit(1)
            if action == "1":
                self.logInAsUser()
            elif action == "2":
                self.createAccount(self.__userService)
            if self.__isLoggedIn:
                self.seeAvailableCars()
        
    def createAccount(self, UserService):
        clearScreen()
        newUser = User()
        newUser.name            = input("Full name: ")
        newUser.email           = input("Email address: ")
        newUser.password        = getpass.getpass("Password: ")
        #passConfirm = input("Confirm password: ")
        newUser.socialNumber    = input("Social security number: ")
        newUser.driverLicense   = input("Driver license ID: ")
        newUser.address         = input("Address: ")
        newUser.phone           = input("Phone number: ")
        newUser.nameOnCard      = input("Name on credit card: ")
        newUser.number          = input("Credit card number: ")
        newUser.cvv             = input("CVV: ")
        newUser.expMonth        = input("Exp month(mm): ")
        newUser.expYear         = input("Exp year(yy): ")
        newUser.Employee        = 1
        UserService.addUser(newUser)
    
    
                
    def logInAsUser(self):
        userEmail = self.getUserEmail()
        if userEmail != "":
            self.getPassword(userEmail) 
        
    
    def getUserEmail(self):
        action = ""
        clearScreen()
        while action != "b":
            action = input("Enter email address: ")
            if(action == "q"):
                exit(1)
            elif self.__userService.getUserByEmail(action) == "Not found":
                clearScreen()
                print("Email address not found!")
            else:
                return action
        return ""

    def getPassword(self, userEmail):
        action = ""
        while action != "b":
            clearScreen()
            if action != "":
                print("Invalid password!")

            print("Enter email address: " + userEmail)
            action = getpass.getpass("Enter password: ")
            selectedUser = self.__userService.getUserByEmail(userEmail)
            if(action == "q"):
                exit(1)

            elif selectedUser.password == action:
                clearScreen()
                self.__currUser = selectedUser
                self.__isLoggedIn = True
                return
