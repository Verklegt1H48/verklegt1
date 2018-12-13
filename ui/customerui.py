from datetime import datetime
from models.car import Car
from models.user import User
from models.order import Order
from services.userservice import UserService
from services.carservice import CarService
from services.orderservice import OrderService
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen
import getpass, sys

class CustomerUI:
    
    def __init__(self):
        self.__userService = UserService()
        self.__carService = CarService()
        self.__orderService = OrderService()
        self.__isLoggedIn = False
        self.__currUser = User()

    def seeAvailableCars(self):
        action = ""
        login = False
        while action != "b":
            clearScreen()
            print("-> See Available Cars")
            if self.__isLoggedIn:
                print("Welcome " + self.__currUser.name + "!")
            else:
                print("You are not logged in!")
            print("These are your options:")
            print("")
            print("1. Sort cars by price/category")
            print("2. Sort cars by manufacturer")
            print("3. Sort cars by availability")
            if self.__isLoggedIn:
                print("b. Go back and log out.")
            else:
                print("b. Go back")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            else:
                print("")
            action = input("Choose an option: ").lower()
            if action == "q":
                exit(1)
            elif action == "1":
                login = self.printCarList("category")
                action = ""
            elif action == "2":
                login = self.printCarList("manufacturer")
                action = ""
            elif action == "3":
                login = self.printCarList("available")
                action = ""
            if login is True:
                break
        return login
        
                 
    def printCarList(self, attribute):
        action = ""
        login  = False
        while action != "b":
            clearScreen()
            carList = self.__carService.getAndSortAvailableCars(attribute)
            counter = 1
            if attribute == "category":
                print("-> Sort cars by price/category")
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
            else:
                print("")
            if self.__isLoggedIn:
                action = input("Please enter which car you wish to book, b to go back or q to quit: ").lower()
            else:
                loginAction = input("Enter \"login\" to go to login screen, b to go back or q to quit: ").lower()
                if loginAction == "login":
                    login = True
                    break
                elif loginAction == "q" or loginAction == "b":
                    action = loginAction
                else:
                    action = "_"
            if action == "q" :
                exit(1)
            if action.isdecimal() and (0 < int(action) < counter):
                carToOrder = carList[int(action) - 1]
                self.inputOrderInfo(carToOrder)
                action = ""
        return login
    
    def inputOrderInfo(self, carToOrder):
        clearScreen()
        print("You chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
        print("Current price is " + str(carToOrder.price) + " isk per day")
        currPrice = str(carToOrder.price)
        currPrice = self.addInsurance(carToOrder)
        clearScreen()
        if(currPrice != ""):
            print("Your total price per day is " + currPrice + " isk")
            pickUpDate = getValidPickUpDate(self.__orderService)
            returnDate = getValidReturnDate(self.__orderService, pickUpDate)
            clearScreen()
            finalPrice = self.__orderService.calcPrice(pickUpDate, returnDate, currPrice)
            print("Your final price is " + str(finalPrice) + " isk")
        paymentMethod = self.selectPaymentMethod()
        if paymentMethod != "":
            newOrder = Order(self.__currUser.id, carToOrder.category, carToOrder.id, paymentMethod, pickUpDate, returnDate)
            self.__orderService.addOrder(newOrder)
            self.orderConfirmation()

    def addInsurance(self, carToOrder):
        action = ""
        while action != "b":
            print("Press q to quit and b to go back")  
            carInsurance = str(int(int(carToOrder.price) / 10))
            if action != "":
                clearScreen()
                print("Invalid input, try again")
            action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")   
            if action == "q" :
                exit(1)
            elif action == "y":    
                totalPrice = str(int(carInsurance) + int(carToOrder.price))
                return totalPrice
            elif action == "n":
                return str(carToOrder.price)
            else:
                pass
        return ""

    def orderConfirmation(self):
        clearScreen()
        action = ""
        while action != "b":
            clearScreen()
            print("Congratulations! Your order has been booked under the name " + self.__currUser.name)
            print("b. Go back to car menu")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                exit(1)
        return

    def selectPaymentMethod(self):
        action = ""
        while action != "b":
            print("-> Select payment method")
            print("These are your options:")
            print("")
            print("1. Debet card")
            print("2. Credit card")
            print("3. Cash")
            print("b. Go back")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                exit(1)
            elif action == "1":
                clearScreen()
                return "DEBET"
            elif action == "2":
                clearScreen()
                return "CREDIT"
            elif action == "3":
                clearScreen()
                return "CASH"
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
                print("Invalid input! Please try again.")
            else:
                print("")
            action = input("Choose an option: ").lower()
            if action == "q" :
                exit(1)
            if action == "1":
                self.logInAsUser()
                if self.__isLoggedIn:
                    self.seeAvailableCars()
                action = ""
            elif action == "2":
                createAccount(self.__userService)
                action = ""
      
    def logInAsUser(self):
        userEmail = self.getUserEmail()
        if userEmail != "":
            self.getPassword(userEmail) 
    
    def getValidPayment(self, order, service):
        isValid = False
        while not isValid:
            clearScreen()
            PayMethod = input("Payment Method: ").upper()
            if service.isValidPayMethod(PayMethod):
                order.payMethod = PayMethod
                isValid = True
            else:
                print("Invalid input. Category must be \"CREDIT\", \"DEBIT\" or \"CASH\"")
                input("Please press enter to try again")

        
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

#validation

def getValidName(userService):
    isValidName = True
    while isValidName:
        name = input("Full name: ")
        clearScreen()
        isValidName = userService.isValidName(name)
    return name

def getValidEmail(userService):
    isValidEmail = True
    while isValidEmail:
        email = input("Email address: ")
        clearScreen()
        isValidEmail = userService.isValidEmail(email)
    return email

def getValidPassword(userService):
    isValidPassword = True
    while isValidPassword:
        password = getpass.getpass("Password: ")
        clearScreen()
        isValidPassword = userService.isValidPassword(password)
        confirmPassword = getpass.getpass("Confirm password: ")
        if confirmPassword == password:
            pass
            clearScreen()
        else:
            clearScreen()
            print("Passwords don't match, please try again")
            isValidPassword = True
    return password

def getValidSocialNumber(userService):
    isValidSocialNumber = True
    while isValidSocialNumber:
        socialNumber = input("Social security number: ")
        clearScreen()
        isValidSocialNumber = userService.isValidSocialNumber(socialNumber)
    return socialNumber

def getValidDriverLicense(userService):
    isValidDriverLicense = True
    while isValidDriverLicense:
        driverLicense = input("Driver license ID: ")
        clearScreen()
        isValidDriverLicense = userService.isValidDriverLicense(driverLicense)
    return driverLicense

def getValidAddress(userService):
    isValidAddress = True
    while isValidAddress:
        address = input("Address: ")
        clearScreen()
        isValidAddress = userService.isValidAddress(address)
    return address

def getValidPhone(userService):
    isValidPhone = True
    while isValidPhone:
        phone = input("Phone number: ")
        clearScreen()
        isValidPhone = userService.isValidPhone(phone)
    return phone

def getValidNameOnCard(userService):
    isValidNameOnCard = True
    while isValidNameOnCard:
        nameOnCard = input("Name on credit card: ")
        clearScreen()
        isValidNameOnCard = userService.isValidNameOnCard(nameOnCard)
    return nameOnCard

def getValidNumber(userService):
    isValidNumber = True
    while isValidNumber:
        number = input("Credit card number: ")
        clearScreen()
        isValidNumber = userService.isValidNumber(number)
    return number

def getValidCvv(userService):
    isValidCvv = True
    while isValidCvv:
        cvv = input("CVV: ")
        clearScreen()
        isValidCvv = userService.isValidCvv(cvv)
    return cvv

def getValidExpMonth(userService):
    isValidExpMonth = True
    while isValidExpMonth:
        expMonth = input("Exp month(mm): ")
        clearScreen()
        isValidExpMonth = userService.isValidExpMonth(expMonth)
    return expMonth

def getValidExpYear(userService, expMonth):
    expYear = input("Exp year(yy): ")
    clearScreen()
    isValidExpYear = userService.isValidExpYear(expYear, expMonth)
    if isValidExpYear == False:
        return "-1"
    else:
        return expYear

def getValidPin(userService):
    isValidPin = True
    while isValidPin:
        pin = input("Pin: ")
        clearScreen()
        isValidPin = userService.isValidPin(pin)
    return pin

def getValidPickUpDate(service):
    action = ""
    while action != "b":
        action = input("When will you pick up your car? (dd/mm/yy): ")
        clearScreen()
        if action == "b" :
            return "", ""
        elif action == "q" :
            sys.exit()
        pickUpCar = service.isValidPickUpDate(action)
        pickUpDate = action
        action = ""
        if pickUpCar == "Year":
            print("You can't order more than a year in advance")
        elif pickUpCar == "Past":
            print("Pick up date must be a future date")
        elif pickUpCar == "Invalid":
            print("Invalid date format")
        else:
            break
    return pickUpDate

def getValidReturnDate(service,pickUpDate): 
    action = ""
    pickUpCar = datetime.strptime(pickUpDate, "%d/%m/%y")    
    while action != "b":
        action = input("When will you return the car? (dd/mm/yy): ")
        clearScreen()
        if action == "b" :
            return "", ""
        elif action == "q" :
            sys.exit()
        returnCar = service.isValidReturnDate(action, pickUpCar)
        if returnCar == "Year":
            print("When will you pick up your car? (dd/mm/yy): " + pickUpDate)
            print("You can't have the car for more than a year")
        elif returnCar == "Past":
            print("When will you pick up your car? (dd/mm/yy): " + pickUpDate)
            print("The car can not be returned before it is picked up")
        elif returnCar == "Invalid":
            print("When will you pick up your car? (dd/mm/yy): " + pickUpDate)
            print("Invalid date format")
        else:
            returnDate = action
            break
    return returnDate

def createStaffAccount(service):
    clearScreen()
    newUser = User()
    newUser.name            = getValidName(service)
    newUser.socialNumber    = getValidSocialNumber(service)
    newUser.pin             = getValidPin(service)
    newUser.employee        = "0" 
    service.addUser(newUser)

def createAccount(service):
    clearScreen()
    newUser = User()
    newUser.name            = getValidName(service)
    newUser.email           = getValidEmail(service)
    newUser.password        = getValidPassword(service)
    newUser.socialNumber    = getValidSocialNumber(service)
    newUser.driverLicense   = getValidDriverLicense(service)
    newUser.address         = getValidAddress(service)
    newUser.phone           = getValidPhone(service)
    newUser.employee        = "1"
    checkDate = True
    while checkDate:
        newUser.nameOnCard  = getValidNameOnCard(service)
        newUser.number      = getValidNumber(service)
        newUser.cvv         = getValidCvv(service)
        newUser.expMonth    = getValidExpMonth(service)
        newUser.expYear     = getValidExpYear(service, newUser.expMonth)
        if newUser.expYear == "-1":
            print("Please try another card")
        else:
            checkDate = False
    service.addUser(newUser)