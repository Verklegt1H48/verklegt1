from models.car import Car
from models.order import Order
from services.carservice import CarService
from services.orderservice import OrderService
from services.userservice import UserService
from models.user import User
from datetime import datetime
from helperfunctions.helpers import clearScreen, getHistory
from ui.headers import printHeader
from ui.customerui import createAccount, modifyUser, getValidReturnDate
from ui.customerui import getValidPickUpDate, getValidSocialNumber, createStaffAccount
import sys
import getpass


class StaffUI:

    def __init__(self):
        self.__carService = CarService()
        self.__orderService = OrderService()
        self.__userService = UserService()
        self.__isLoggedIn = False
        self.__userName = ""

    # First menu that a staff member sees after login
    def staffMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->Staff menu")
            print("Welcome " + self.__userName + "!")
            print("These are your options")
            print("")
            print("1. Car management")
            print("2. User management")
            print("3. Order management")
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
                self.staffCarMenu()
                action = ""
            elif action == "2":
                self.staffCustomerMenu()
                action = ""
            elif action == "3":
                self.orderMenu()
                action = ""

    # The car menu shows staff members the options that are avaliable to them
    def staffCarMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->Car menu")
            print("")
            print("These are your options:")
            print("")
            print("1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
            print("4. List rent history for a car")
            print("5. Return car")
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
                action = ""
                self.addCar()
            elif action == "2":
                action = ""
                self.removeCar()
            elif action == "3":
                action = ""
                clearScreen()
                print("-> List all cars")
                print("")
                print("These are all the cars:")
                printHeader("carSelect")
                cars = self.__carService.getCarList()
                for car in cars:
                    if car.deleted != 1:
                        print("{:5}{}".format(str(car.id), car))
                print("")
                input("Press enter to return ")
            elif action == "4":
                carId = ""
                while carId != "b":
                    clearScreen()
                    print("->List rent history for a car")
                    if carId != "":
                        print("Invalid input! Please try again.")
                    else:
                        print("")
                    carId = input("Please enter a car ID or \"b\" to go back: ")
                    if carId == "q":
                        sys.exit()
                    elif self.getValidCarId(carId, self.__carService):
                        getHistory(self.__orderService.getOrdersByStatus(1), carId, "car")
                        carId = "b"
            elif action == "5":
                clearScreen()
                printHeader("carSelect")
                cars = self.__carService.getCarList()
                self.markCarAvailable(cars)
                action = ""

    # The staff menu for looking up, altering and adding customers
    def staffCustomerMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->User menu")
            print("")
            print("These are your options")
            print("")
            print("1. Add a customer")
            print("2. Remove a user")
            print("3. List all customers")
            print("4. Add a new staff member")
            print("5. List all staff members")
            print("6. Find user by social security number")
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
                createAccount(self.__userService)
                action = ""
            elif action in ("2"):
                clearScreen()
                self.removeUser()
                action = ""
            elif action in ("3", "5"):
                clearScreen()
                self.printUsers(action)
                action = ""
            elif action == "4":
                action = ""
                createStaffAccount(self.__userService)
                clearScreen()
            elif action == "6":
                self.printUserBySocial()

    # The staff interface for looking up orders or adding a new order
    def orderMenu(self):
        action = ""
        while action != "b":
            clearScreen()
            print("->User menu")
            print("")
            print("These are your options")
            print("")
            print("1. New order")
            print("2. List confirmed orders")
            print("3. List unconfirmed orders")
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
                self.addOrder()
                action = ""
            elif action == "2":
                clearScreen()
                self.printOrderList(1)
                action = ""
            elif action == "3":
                clearScreen()
                self.printOrderList(0)
                action = ""

    # A function that enables staff members to make a specific car avaliable
    def markCarAvailable(self, cars):
        action = ""
        id = ""
        while action != "b":
            clearScreen()
            printHeader("carSelect")
            cars = self.__carService.getCarList()
            for car in cars:
                if car.available != 1:
                    print("{:5}{}".format(str(car.id), car))
            if action != "":
                print("No car with carID \"{}\" exists".format(id))
            else:
                print("")
            id = input("Enter the ID of the car you want to mark as available: ")
            if id == "q":
                sys.exit()
            if id == "b":
                break
            if self.getValidCarId(id, self.__carService,):
                newMileage = self.validateMileageToUpdate(self.__carService, id)
                if newMileage == "b":
                    return
                action = input("Are you sure you want to mark car with ID \"{}\" available? y/n: ".format(id)).lower()
                while action not in ("b", "y", "n", "q"):
                    action = input("Please input \"y\" or \"n\"!: ").lower()
                clearScreen()
                if action == "y":
                    if self.__carService.makeCarAvailable(id, newMileage):
                        print("Car with ID \"{}\" is now available".format(id))
                        input("Press enter to continue")
                    else:
                        print("No car with ID: \"{}\" exists. Please try again".format(id))
                        input("Press enter to continue")
                if action == "n":
                    print("You aborted the deletion of the car with ID: \"{}\"".format(id))
                    input("Press enter to continue")
                if action == "q":
                    sys.exit()
            else:
                action = "noID"

    # Prints out the order list
    def printOrderList(self, status):
        action = ""
        while action != "b":
            clearScreen()
            if status == 0:
                print("->List all unconfirmed orders")
            else:
                print("->List all confirmed orders")
            print("")
            print("These are the orders you wanted to view:")
            orderList = self.__orderService.getOrdersByStatus(status)
            counter = 1
            printHeader("orderSelect")
            for order in orderList:
                print("{:8}{}".format(str(counter), order))
                counter += 1
            if action != "":
                print("Invalid input! Please try again.")
            print("Press b to return to the previous page")
            print("Press q to quit")
            action = input("Please select the order you wish to view: ").lower()
            if action == "q":
                exit(1)
            elif action.isdecimal() == False:
                pass
            elif int(action) >= counter:
                pass
            elif int(action) <= 0:
                pass
            else:
                self.inputOrderInfo(orderList[int(action) - 1], action)
                action = ""
                del orderList

    # Function to print out either the user or staff member lists
    def printUsers(self, action):
        users = self.__userService.getUserList()
        clearScreen()
        if action == "3":
            isStaff = "1"
            print("->List all customers")
            print("")
            print("These are all the customers:")
            printHeader("userSelect")
        else:
            isStaff = "0"
            print("->List all staff members")
            print("")
            print("These are all the staff members:")
            printHeader("staffSelect")
        for user in users:
            if str(user.employee) == isStaff and str(user.deleted) == "0":
                print(user)
        input("Press enter to return: ")

    # View of a single order
    def inputOrderInfo(self, orderToChange, number):
        pass
        action = ""
        while action != "b":
            clearScreen()
            print("->View a single order")
            print("The unique ID of the order you selected is \"{}\"".format(str(orderToChange.id)))
            if orderToChange.status == 1:
                orderStatus = "confirmed"
            else:
                orderStatus = "unconfirmed"
            print("This order is " + orderStatus)
            print("This order was assigned a car in category: " + str(orderToChange.carCategory))
            print("")
            print("1. Modify order")
            print("2. To delete order")
            if orderToChange.status == 0:
                print("3. To assign a new car to this order")
                pickUpCar = datetime.strptime(orderToChange.pickUpDate, "%d/%m/%y").date()
                if pickUpCar == datetime.today().date():
                    print("4. To confirm order")
            print("b. Go back")
            print("q. Exit the program")
            if action != "":
                print("Invalid input! Please try again.")
            else:
                print("")
            action = input("Choose an option: ").lower()
            if action == "q":
                sys.exit()
            elif action == "1":
                self.modifyOrder(orderToChange, number)
                action = "b"
            elif action == "2":
                self.__orderService.deleteOrder(orderToChange.id)
                action = "b"
            elif action == "3" and orderToChange.status == 0:
                self.carAssignment(orderToChange)
                action = "b"
            elif action == "4" and orderToChange.status == 0 and pickUpCar == datetime.today().date():
                self.__orderService.confirmOrder(orderToChange.id)
                action = "b"

    # Menu that show what staff members can modify in a customers order
    def modifyOrder(self, order, number):
        action = ""
        while action != "b":
            clearScreen()
            print("->Order modification")
            print("")
            print("This is the order you have chosen for modification:")
            printHeader("orderSelect")
            print(str(number) + str(order))
            print("")
            print("Select what you would like to modify")
            print("1. Car category")
            print("2. Payment method")
            print("3. Pick up date")
            print("4. Return date")
            print("b. Go back")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            else:
                print("")
            action = input("Please select what you wish to change: ").lower()
            if action == "q":
                sys.exit()
            elif action == "1":
                self.getValidCarCategory(order, self.__carService)
                car = self.carSelectionByCategory(order.carCategory)
                if car == "b":
                    continue
                order.carId = car.id
                action = ""
            elif action == "2":
                self.getValidPayment(order, self.__orderService)
                action = ""
            elif action == "3":
                order.pickUpDate = getValidPickUpDate(self.__orderService, order.returnDate, "Update")
                action = ""
            elif action == "4":
                order.returnDate = getValidReturnDate(self.__orderService, order.pickUpDate)
                action = ""
            self.__orderService.updateOrder(order)

    # Adds a car to an unconfirmed order
    def carAssignment(self, order):
        car = self.__carService.getFirstAvailableCarByCategory(order.carCategory)
        if car == None:
                print("\n ***No car available in that category***\n")
                input("Press enter to go back")
                return
        print("\n Manufacturer: {} , {}\n Year: {}\n Mileage: {}\n Seats: {}\n Transmission: {}\n Extras: {}"
              .format(car.manufacturer, str(car.model), str(car.year), str(car.mileage), str(car.seats),
                      car.transmission, str(car.extras).strip("[']").replace("', '", ", ")))
        action = ""
        while action != "b":
            action = input("Would you like to assign this car to the order Y/N: ").lower()
            if action == "q":
                sys.exit()
            if action == "y":
                self.__orderService.assignCarToOrder(car, order)
                action = "b"
            elif action == "n":
                car = self.carSelectionByCategory(order.carCategory)
                if car == "b":
                    action = "b"
                self.__orderService.assignCarToOrder(car, order)
                action = "b"
            if action != "":
                print("Invalid input! Please try again.")

    # Prints out cars in order of category
    def carSelectionByCategory(self, category):
        action = ""
        while action != "b":
            clearScreen()
            carList = self.__carService.getAvailableCarsByCategory(category)
            if carList == []:
                print("No Car available in that category")
                input("Press enter to start over: ")
                return "b"
            counter = 0
            printHeader("carSelect")
            for car in carList:
                counter += 1
                print("{:5}{}".format(str(counter), car))
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Please select the car you wish to book or b to start over: ").lower()
            if action == "q":
                exit(1)
            elif action.isdecimal() and (0 < int(action) <= int(counter)):
                return carList[int(action) - 1]
        return "b"

    # Add a car function for staff members
    def addCar(self):
        newCar = Car()
        if self.getValidCategory(newCar, self.__carService) == "b":
            return
        if self.getValidManufacturer(newCar, self.__carService) == "b":
            return
        if self.getValidModel(newCar, self.__carService) == "b":
            return
        if self.getValidYear(newCar, self.__carService) == "b":
            return
        if self.getValidMileage(newCar, self.__carService) == "b":
            return
        if self.getValidSeats(newCar, self.__carService) == "b":
            return
        if self.getValidTransmission(newCar, self.__carService) == "b":
            return
        if self.getValidExtras(newCar, self.__carService) == "b":
            return
        self.__carService.addCar(newCar)
        input("You have successfully added a new car. Please press enter to continue")

    # Function to remove a car
    def removeCar(self):
        clearScreen()
        choice = ""
        id = input("Enter the ID of the car you want to delete: ")
        if id == "q":
            sys.exit()
        if id == "b":
            return
        choice = input("Are you sure you want to delete car with ID: \"{}\"? y/n: ".format(id)).lower()
        while choice not in ("b", "y", "n", "q"):
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

    # Function to remove a user
    def removeUser(self):
        clearScreen()
        choice = ""
        id = input("Enter the ID of the user you want to delete: ")
        if id == "q":
            sys.exit()
        if id == "b":
            return
        choice = input("Are you sure you want to delete user with ID: \"{}\"? y/n: ".format(id)).lower()
        while choice not in ("b", "y", "n", "q"):
            choice = input("Please input \"y\" or \"n\"!: ").lower()
        clearScreen()
        if choice == "y":
            if self.__userService.deleteUser(id):
                print("You have deleted the user with ID: \"{}\"".format(id))
                input("Press enter to continue")
            else:
                print("No user with ID: \"{}\" exists. Please try again".format(id))
                input("Press enter to continue")
        if choice == "n":
            print("You aborted the deletion of the user with ID: \"{}\"".format(id))
            input("Press enter to continue")
        if choice == "q":
            sys.exit()

    # Function to add an order
    def addOrder(self):
        newOrder = Order()
        if self.getValidUserId(newOrder, self.__userService) == "b":
            return
        self.getValidCarCategory(newOrder, self.__carService)
        car = self.carSelectionByCategory(newOrder.carCategory)
        if car == "b":
            return
        newOrder.carId = car.id
        if self.getValidPayment(newOrder, self.__orderService) == "b":
            return
        pickUpDate = getValidPickUpDate(self.__orderService, "", "New")
        if pickUpDate == "":
            return
        else:
            newOrder.pickUpDate = pickUpDate
        returnDate = getValidReturnDate(self.__orderService, newOrder.pickUpDate)
        if returnDate == "":
            return
        else:
            newOrder.returnDate = returnDate
        self.__orderService.addOrder(newOrder)

    def logInAsStaff(self):
        staffSocial = self.getStaffSocial()
        if staffSocial != "":
            self.getStaffPin(staffSocial)
            if self.__isLoggedIn:
                self.staffMenu()

    # Function for staff members to look up specific staff members based on social security number
    def getStaffSocial(self):
        clearScreen()
        social = ""
        while social != "b":
            social = input("Enter your social security number: ").lower()
            selectedUser = self.__userService.getUserBySocial(social)
            if(social == "q"):
                sys.exit()
            elif selectedUser == "Not found":
                clearScreen()
                print("Social security number not valid")
            else:
                if selectedUser.employee == "0":
                    return social
                else:
                    clearScreen()
                    print("Social security number not valid")
        return ""

    def getStaffPin(self, staffSocial):
        action = ""
        while action != "b":
            clearScreen()
            if action != "":
                print("Unique employee number not found")
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

    # Function for staff members to search for users based on social security number
    def printUserBySocial(self):
        social = ""
        user = ""
        while social != "b":
            clearScreen()
            print("->Find user by social security number")
            if social != "":
                print("No user found with the social security number: {}".format(social))
            else:
                print("")
            social = input("Please enter a social security number or \"b\" to go back: ").lower()
            user = self.__userService.getUserBySocial(social)
            if user == "Not found":
                pass
            else:
                self.userOptions(user)

    def userOptions(self, user):
        action = ""
        while action != "b":
            clearScreen()
            print("->Find user by social security number")
            print("")
            print("This is the user you asked for:")
            if user.employee == "1":
                printHeader("userSelect")
            else:
                printHeader("staffSelect")
            print(user)
            print("")
            print("1. Modify user")
            print("2. Print user history")
            print("Press b to go back")
            print("Press q to quit")
            if action != "":
                if action == "1":
                    print("You can't modify an employee!")
                else:
                    print("Invalid input! Please try again.")
            action = ""
            action =input("Choose an option: ")
            if action == "q":
                sys.exit()
            if action == "1":
                if user.employee == "0":
                    pass
                else:
                    modifyUser(self.__userService, user)
            if action == "2":
                getHistory(self.__orderService.getOrdersByStatus(1), user.id, "user")
    # Validation functions

    def getValidCategory(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            category = input("Category: ").upper()
            if category == "Q":
                sys.exit()
            if service.isValidCategory(category):
                car.category = category
                isValid = True
                if category == "A":
                    car.price = "5000"
                elif category == "B":
                    car.price = "10000"
                elif category == "C":
                    car.price = "15000"
                else:
                    car.price = "20000"
            else:
                print("Invalid input. Category must be \"A\", \"B\", \"C\" or \"D\"")
                input("Press any key to try again: ")

    def getValidCarId(self, id, service):
        return service.isValidCarId(id)


    def getValidCarCategory(self, order, service):
        isValid = False
        while not isValid:
            clearScreen()
            category = input("Car Category: ").upper()
            if category == "Q":
                sys.exit()
            if service.isValidCategory(category):
                order.carCategory = category
                isValid = True
            else:
                print("Invalid input. Category must be \"A\", \"B\", \"C\" or \"D\"")
                input("Press any key to try again: ")

    def getValidPayment(self, order, service):
        isValid = False
        while not isValid:
            clearScreen()
            payMethod = input("Payment Method: ").upper()
            if payMethod == "Q":
                sys.exit()
            if payMethod == "B":
                return "b"
            if service.isValidPayMethod(payMethod):
                clearScreen()
                order.payMethod = payMethod
                isValid = True
            else:
                print("Invalid input. Category must be \"CREDIT\", \"DEBIT\" or \"CASH\"")
                input("Press any key to try again: ")

    def getValidUserId(self, order, service):
        isValid = False
        while not isValid:
            clearScreen()
            userId = input("User ID: ")
            if userId == "q":
                sys.exit()
            if userId == "b":
                return "b"
            if service.isValidUserId(userId):
                order.userId = userId
                isValid = True
            else:
                print("Invalid input. User ID not found")
                input("Please press enter to try again")

    def getValidManufacturer(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            manufacturer = input("Manufacturer: ")
            if manufacturer == "q":
                sys.exit()
            if manufacturer == "b":
                return "b"
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
            if model == "q":
                sys.exit()
            if model == "b":
                return "b"
            elif service.isValidModel(model):
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
            if year == "q":
                sys.exit()
            elif year == "b":
                return "b"
            elif service.isValidYear(year):
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
            if mileage == "q":
                sys.exit()
            elif mileage == "b":
                return "b"
            elif service.isValidMileage(mileage):
                car.mileage = mileage
                isValid = True
            else:
                print("Invalid input. Mileage must be an integer between 0 and 1000000")
                input("Please press enter to try again")

    def validateMileageToUpdate(self, service, carId):
        isValid = False
        car = service.getCarById(carId)
        while not isValid:
            clearScreen()
            mileage = input("Input current mileage of the car: ")
            if mileage == "b":
                return "b"
            elif mileage == "q":
                sys.exit()
            elif service.isValidMileage(mileage, car):
                return mileage
            else:
                print("Invalid input. The mileage must be between " + str(car.mileage) + " and 1000000")
                input("Please press enter to try again")

    def getValidSeats(self, car, service):
        isValid = False
        while not isValid:
            clearScreen()
            seats = input("Seats: ")
            if seats == "q":
                sys.exit()
            if seats == "b":
                return "b"
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
            if transmission == "Q":
                sys.exit()
            elif transmission == "B":
                return "b"
            elif service.isValidTransmission(transmission):
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
            if extras == "q":
                sys.exit()
            elif extras == "b":
                return "b"
            elif service.isValidExtras(extras):
                car.extras = extras
                isValid = True
            else:
                print("Invalid input. Extras must be less than 40 letters long")
                input("Please press enter to try again")
