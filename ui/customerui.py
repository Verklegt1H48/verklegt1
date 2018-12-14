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

    # Menu that show the user how they can sort the cars
    def seeAvailableCars(self):
        action = ""
        login = False
        while action != "b":
            clearScreen()
            print("-> Browse Cars")
            if self.__isLoggedIn:
                print("Welcome " + self.__currUser.name + "!")
            else:
                print("")
            print("These are your options:")
            print("")
            print("1. Sort cars by price/category")
            print("2. Sort cars by manufacturer")
            print("3. See available cars")
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
                sys.exit()
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

    # Prints the lists of sorted cars
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
                print("-> See available cars")
            if self.__isLoggedIn:
                print("")
            else:
                print("You are not logged in. You need to login to book a car.")
            print("These are the cars you have chosen to see:")
            printHeader("carSelect")
            for car in carList:
                print("{:5}{}".format(str(counter),car))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            else:
                print("")
            if self.__isLoggedIn:
                action = input("Please enter which car you wish to book, b to go back or q to exit the program: ").lower()
            else:
                loginAction = input("Enter \"login\" to go to login screen, b to go back or q to exit the program: ").lower()
                if loginAction == "login":
                    login = True
                    break
                elif loginAction == "q" or loginAction == "b":
                    action = loginAction
                else:
                    action = "_"
            if action == "q" :
                sys.exit()
            if action.isdecimal() and (0 < int(action) < counter):
                carToOrder = carList[int(action) - 1]
                self.inputOrderInfo(carToOrder)
                action = ""
        return login
    
    # Gather information about the order
    def inputOrderInfo(self, carToOrder):        
        clearScreen()
        print("->Rent a car")
        print("At any time during the process can you press b to go back to the car menu or q to quit")
        print("You requested the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
        print("Current price is " + str(carToOrder.price) + " isk per day")
        currPrice = str(carToOrder.price)
        currPrice = self.addInsurance(carToOrder)
        if currPrice == "b":
            return
        clearScreen()
        if currPrice != "":
            print("Your total price per day is " + currPrice + " isk")
            pickUpDate = getValidPickUpDate(self.__orderService, "", "New")
            if pickUpDate == "":
                return
            returnDate = getValidReturnDate(self.__orderService, pickUpDate)
            if returnDate == "":
                return
            finalPrice = self.__orderService.calcPrice(pickUpDate, returnDate, currPrice)
            print("Your final price is " + str(finalPrice) + " isk")
            input("Please press enter to continue")
            clearScreen()
        paymentMethod = selectPaymentMethod()
        if paymentMethod != "":
            newOrder = Order(self.__currUser.id, carToOrder.category, carToOrder.id, paymentMethod, pickUpDate, returnDate)
            self.__orderService.addOrder(newOrder)
            self.orderConfirmation(newOrder)

    # This prompts if the user wants an insurance
    def addInsurance(self, carToOrder):
        action = ""
        while action != "b":
            carInsurance = str(int(int(carToOrder.price) / 10))
            if action != "":
                clearScreen()
                print("Invalid input. Please enter \"y\" or \"n\"")
            action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")   
            if action == "q" :
                sys.exit()
            if action == "b":
                return "b"
            elif action == "y":    
                totalPrice = str(int(carInsurance) + int(carToOrder.price))
                return totalPrice
            elif action == "n":
                return str(carToOrder.price)
            else:
                pass
        return ""

    # Feedback for when the user has successfully made an order
    def orderConfirmation(self, order):
        clearScreen()
        action = ""
        while action != "b":
            clearScreen()
            print("->Order confirmation!")
            print("")
            print("Congratulations and thank you!")
            print("Your order has been booked under the name {}".format(self.__currUser.name))
            print("with {} as the preferred payment method.".format(order.payMethod.lower()))
            print("The car you requested is in category: {}. If it is not available when your".format(order.carCategory))
            print("pick up date arrives you will get another car in the same category.")
            print("The creditcard stored in your account has been used for confirmation")
            print("and will NOT be charged unless you do not show up for your order.")
            print("If you have any questions or would like to change your order do not hesitate to")
            print("contact the car rental in phone +354 462-1840 or by email staff@santasrental.is")
            print("")
            print("b. Go back to car menu")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            if action == "q":
                sys.exit()
        return

   
    # Show avaliable options within the customer menu              
    def customerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->Customer login screen")
            print("")
            print("These are your options")
            print("")
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
                sys.exit()
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

    def getUserEmail(self):
        action = ""
        clearScreen()
        while action != "b":
            action = input("Enter email address: ")
            if(action == "q"):
                sys.exit()
            elif self.__userService.getUserByEmail(action) == "Not found" or action == "":
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
                sys.exit()

            elif selectedUser.password == action:
                clearScreen()
                self.__currUser = selectedUser
                self.__isLoggedIn = True
                return

#validation functions

def getValidName(userService):
    isValidName = False
    while not isValidName:
        name = input("Full name: ")
        clearScreen()
        error = userService.isValidName(name)
        if error == "length":
            print("Invalid name length")
        else:
            isValidName = True
    return name

def getValidEmail(userService):
    isValidEmail = False
    while not isValidEmail:
        email = input("Email address: ")
        clearScreen()
        error = userService.isValidEmail(email)
        if error == "invalid":
            print("Invalid email address! Please enter a valid email address")
        else: 
            isValidEmail = True
    return email

def getValidPassword(userService):
    isValidPassword = False
    while not isValidPassword:
        password = getpass.getpass("Password: ")
        clearScreen()
        error = userService.isValidPassword(password)
        if error == "short":
            print("Passwords must be at least 8 characters long")
        elif error == "long":
            print("Password is too long")
        else:
            confirmPassword = getpass.getpass("Confirm password: ")
            clearScreen()
            if confirmPassword == password:
                isValidPassword = True
            else:       
                print("Passwords don't match, please try again")
    return password

def getValidSocialNumber(userService):
    isValidSocialNumber = False
    while not isValidSocialNumber:
        socialNumber = input("Social security number: ")
        clearScreen()
        error = userService.isValidSocialNumber(socialNumber)
        if error == "numbers":
            print("Social security number can only contain numbers")
        elif error == "length":
            print("Social security number must be 10 digits long")
        else:
            isValidSocialNumber = True
    return socialNumber

def getValidDriverLicense(userService):
    isValidDriverLicense = False
    while not isValidDriverLicense:
        driverLicense = input("Driver license ID: ")
        clearScreen()
        error = userService.isValidDriverLicense(driverLicense)
        if error == "numbers":
            print("Driver license ID can only contain numbers")
        elif error == "length":
            print("Driver license ID must be 9 digits long")
        else:
            isValidDriverLicense = True
    return driverLicense

def getValidAddress(userService):
    isValidAddress = False
    while not isValidAddress:
        address = input("Address: ")
        clearScreen()
        error = userService.isValidAddress(address)
        if error == "invalid":
            print("Invalid address!")
        else:
            isValidAddress = True
    return address

def getValidPhone(userService):
    isValidPhone = False
    while not isValidPhone:
        phone = input("Phone number: ")
        clearScreen()
        error = userService.isValidPhone(phone)
        if error == "numbers":
            print("Phone number can only contain numbers")
        elif error == "length":
            print("Phone number must be at least 7 digits long")
        else:
            isValidPhone = True
    return phone

def getValidNameOnCard(userService):
    isValidNameOnCard = False
    while not isValidNameOnCard:
        nameOnCard = input("Name on credit card: ")
        clearScreen()
        error = userService.isValidNameOnCard(nameOnCard)
        if error == "length":
            print("Invalid name length")
        else:
            isValidNameOnCard = True
    return nameOnCard

def getValidNumber(userService):
    isValidNumber = False
    while not isValidNumber:
        number = input("Credit card number: ")
        clearScreen()
        error = userService.isValidNumber(number)
        if error == "numbers":
            print("Credit card number can only contain numbers")
        elif error == "length":
            print("Credit card number must be 16 digits long")
        else:
            isValidNumber = True
    return number

def getValidCvv(userService):
    isValidCvv = False
    while not isValidCvv:
        cvv = input("CVV: ")
        clearScreen()
        isValidCvv = userService.isValidCvv(cvv)
        if isValidCvv == "numbers":
            print("CVV code can only contain numbers")
            isValidCvv = False
        if isValidCvv == "length":
            print("CVV code must be 3 digits long")
            isValidCvv = False
    return cvv

def getValidExpMonth(userService):
    isValidExpMonth = False
    while not isValidExpMonth:
        expMonth = input("Exp month(mm): ")
        clearScreen()
        isValidExpMonth = userService.isValidExpMonth(expMonth)
        if isValidExpMonth == "NaN":
            print("Please enter a number")
            isValidExpMonth = False
        elif isValidExpMonth == "length":
            print("Invalid input!")
            isValidExpMonth = False
        elif isValidExpMonth == "month":
            print("Month does not exist")
            isValidExpMonth = False
    return expMonth

def getValidExpYear(userService, expMonth):
    isValidExpYear = False
    while not isValidExpYear:
        expYear = input("Exp year(yy): ")
        clearScreen()
        error = userService.isValidExpYear(expYear, expMonth)
        if error == "NaN":
            print("Please enter a number")
        elif error == "length":
            print("Invalid input!")
        elif error == "year":
            print("Card is expired")
            return "-1"
        else:
            return expYear

def getValidPin(userService):
    isValidPin = False
    while not isValidPin:
        pin = input("Pin: ")
        clearScreen()
        isValidPin = userService.isValidPin(pin)
        if isValidPin == "numbers":
            print("Pin can only contain numbers")
            isValidPin = False
        elif isValidPin == "length":
            print("Employee pin must be 5 digits long")
            isValidPin = False
    return pin

def getValidPickUpDate(service, returnDate, flag):
    action = ""
    while action != "b":
        if flag == "Update":
            print("Current return date is: {}".format(returnDate))
        action = input("When will the car be picked up? (dd/mm/yy): ")
        clearScreen()
        if action == "b" :
            return ""
        elif action == "q" :
            sys.exit()
        pickUpCar = service.isValidPickUpDate(action, returnDate, flag)
        pickUpDate = action
        if pickUpCar == "Year":
            print("Pick up date can't be more than a year in advance")
        elif pickUpCar == "Past":
            print("Pick up date must be a future date")
        elif pickUpCar == "Invalid":
            print("Invalid date format")
        elif pickUpCar == "":
            print("Pick up date can't be on or after the return date")
        else:
            break
    return pickUpDate

def getValidReturnDate(service,pickUpDate): 
    action = ""
    pickUpCar = datetime.strptime(pickUpDate, "%d/%m/%y")    
    while action != "b":
        print("When will the car be picked up? (dd/mm/yy): " + pickUpDate)
        action = input("Enter return date? (dd/mm/yy): ")
        if action == "b" :
            return ""
        elif action == "q" :
            sys.exit()
        returnCar = service.isValidReturnDate(action, pickUpCar)
        if returnCar == "Year":
            clearScreen()
            print("You can't have the car for more than a year")
        elif returnCar == "Past":
            clearScreen()
            print("The car can not be returned before it is picked up")
        elif returnCar == "Invalid":
            clearScreen()
            print("Invalid date format")
        else:
            returnDate = action
            break
    return returnDate

# The interface for staff members to modify and update specific information about customers 
def modifyUser(service, user):
        action = ""
        while action != "b":
            print("->Modify user")
            clearScreen()
            print("->Modify user")
            print("")
            printHeader("userSelect")
            print(user)
            print("")
            print("Select what you would like to modify")
            print("1. Email")
            print("2. Password")
            print("3. Drivers License number")
            print("4. Address")
            print("5. Phone number")
            print("6. Card info")
            print("b. Go back")
            print("q. Exit program")
            if action != "":
                print("Invalid input, try again")
            else:
                print("")
            action = input("Please select what you wish to change: ").lower()
            clearScreen()
            if action == "q":
                sys.exit()
            elif action == "1" :
                user.email = getValidEmail(service)
                action = ""
            elif action == "2" :
                oldPass = ""
                while oldPass != user.password:
                    clearScreen()
                    oldPass = getpass.getpass("Input old password :")
                user.password = getValidPassword(service)
                action = ""
            elif action == "3":
                user.driverLicense= getValidDriverLicense(service)
                action = ""
            elif action == "4" :
                user.address = getValidAddress(service)
                action = ""
            elif action == "5" :
                user.phone = getValidPhone(service)
                action = ""
            elif action == "6" :
                user = addCreditCard(user, service)
                action = ""
            service.updateUser(user)

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
    newUser = addCreditCard(newUser, service)
    service.addUser(newUser)

def addCreditCard(newUser, service):
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
    return newUser

 # Allows the user to select a payment method
def selectPaymentMethod():
    action = ""
    while action != "b":
        clearScreen()
        print("Please select a payment method:")
        print("")
        print("1. Debet card")
        print("2. Credit card")
        print("3. Cash")
        print("b. Go back")
        print("q. Exit program")
        if action != "":
            print("Invalid input! Please try again.")
        else:
            print("")
        action = input("Choose an option: ").lower()
        if action == "q":
            sys.exit()
        elif action == "1":
            clearScreen()
            return "DEBET"
        elif action == "2":
            clearScreen()
            return "CREDIT"
        elif action == "3":
            clearScreen()
            return "CASH"
    return action
