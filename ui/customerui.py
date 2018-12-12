from datetime import datetime
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
            print("-> See Available Cars")
            if self.__isLoggedIn:
                print("Welcome " + self.__currUser.name + "!")
            else:
                print("You are not logged in!")
            print("These are your options:")
            print("")
            print("1. Sort cars by Price")
            print("2. Sort cars by manufacturer")
            print("3. Sort cars by availability")
            print("4. Sort cars by Category")
            print("b. Go back")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                exit(1)
            elif action in ("1", "4"):
                self.printCarList("category")
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
            if attribute == "category":
                print("-> Sort cars by price category")
            if attribute == "manufacturer":
                print("-> Sort cars by manufacturer")
            if attribute == "available":
                print("-> Sort cars by availability")
            if self.__isLoggedIn:
                print("You are logged in as: {}".format(self.__currUser.name))
            else:
                print("You are not logged in. You need to login to book a car.")
            print("These are the cars you have chosen to see:")
            printHeader("carSelect")
            for car in carList:
                print("{:5}{}".format(counter,car))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            if self.__isLoggedIn:
                action = input("Please enter which car you wish to book, b to go back or q to quit: ").lower()
            else:
                action = input("Enter \"login\" to go to login screen, b to go back or q to quit: ")
                if action == "login":
                    self.customerMenu()
                    action = ""
            if action == "q" :
                exit(1)
            if action.isdecimal() and (0 < int(action) < counter):
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
                print("Your total price per day is " + str(carToOrder.price) + " isk")
                return carToOrder.price
            else:
                pass
        return ""
                    
    def customerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->Customer login screen")
            print("")
            print("These are your options")
            print("1. Log in")
            print("2. Sign up")
            print("b. Go back")
            print("q. Exit program") 
            if action != "":
                print("Invalid input, try again")
            action = input("Choose an option: ").lower()
            if action == "q" :
                exit(1)
            if action == "1":
                action = ""
                self.logInAsUser()
            elif action == "2":
                action = ""
                self.createAccount(self.__userService)
            if self.__isLoggedIn:
                self.seeAvailableCars()
    
                
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


    def createAccount(self, UserService):
        clearScreen()
        newUser = User()
        newUser.name            = self.getValidName()
        newUser.email           = self.getValidEmail()
        newUser.password        = self.getValidPassword()
        newUser.socialNumber    = self.getValidSocialNumber()
        newUser.driverLicense   = self.getValidDriverLicense()
        newUser.address         = self.getValidAddress()
        newUser.phone           = self.getValidPhone()
        newUser.Employee        = 1
        checkDate = True
        while checkDate:
            newUser.nameOnCard  = self.getValidNameOnCard()
            newUser.number      = self.getValidNumber()
            newUser.cvv         = self.getValidCvv()
            newUser.expMonth    = self.getValidExpMonth()
            newUser.expYear     = self.getValidExpYear(newUser.expMonth)
            if newUser.expYear == "-1":
                print("Please try another card")
            else:
                checkDate = False
        UserService.addUser(newUser)

    def getValidName(self):
        isValidName = True
        while isValidName:
            name = input("Full name: ")
            clearScreen()
            isValidName = self.__userService.isValidName(name)
        return name

    def getValidEmail(self):
        isValidEmail = True
        while isValidEmail:
            email = input("Email address: ")
            clearScreen()
            isValidEmail = self.__userService.isValidEmail(email)
        return email

    def getValidPassword(self):
        isValidPassword = True
        while isValidPassword:
            password = getpass.getpass("Password: ")
            clearScreen()
            isValidPassword = self.__userService.isValidPassword(password)
            confirmPassword = getpass.getpass("Confirm password: ")
            if confirmPassword == password:
                pass
                clearScreen()
            else:
                clearScreen()
                print("Passwords don't match, please try again")
                isValidPassword = True
        return password

    def getValidSocialNumber(self):
        isValidSocialNumber = True
        while isValidSocialNumber:
            socialNumber = input("Social security number: ")
            clearScreen()
            isValidSocialNumber = self.__userService.isValidSocialNumber(socialNumber)
        return socialNumber

    def getValidDriverLicense(self):
        isValidDriverLicense = True
        while isValidDriverLicense:
            driverLicense = input("Driver license ID: ")
            clearScreen()
            isValidDriverLicense = self.__userService.isValidDriverLicense(driverLicense)
        return driverLicense

    def getValidAddress(self):
        isValidAddress = True
        while isValidAddress:
            address = input("Address: ")
            clearScreen()
            isValidAddress = self.__userService.isValidAddress(address)
        return address

    def getValidPhone(self):
        isValidPhone = True
        while isValidPhone:
            phone = input("Phone number: ")
            clearScreen()
            isValidPhone = self.__userService.isValidPhone(phone)
        return phone

    def getValidNameOnCard(self):
        isValidNameOnCard = True
        while isValidNameOnCard:
            nameOnCard = input("Name on credit card: ")
            clearScreen()
            isValidNameOnCard = self.__userService.isValidNameOnCard(nameOnCard)
        return nameOnCard

    def getValidNumber(self):
        isValidNumber = True
        while isValidNumber:
            number = input("Credit card number: ")
            clearScreen()
            isValidNumber = self.__userService.isValidNumber(number)
        return number
    
    def getValidCvv(self):
        isValidCvv = True
        while isValidCvv:
            cvv = input("CVV: ")
            clearScreen()
            isValidCvv = self.__userService.isValidCvv(cvv)
        return cvv

    def getValidExpMonth(self):
        isValidExpMonth = True
        while isValidExpMonth:
            expMonth = input("Exp month(mm): ")
            clearScreen()
            isValidExpMonth = self.__userService.isValidExpMonth(expMonth)
        return expMonth

    def getValidExpYear(self, expMonth):
        expYear = input("Exp year(yy): ")
        clearScreen()
        isValidExpYear = self.__userService.isValidExpYear(expYear, expMonth)
        if isValidExpYear == False:
            return "-1"
        else:
            return expYear
    
