from models.car import Car
from services.carservice import CarService
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__carService = CarService()
        self.__action = ""
    def mainMenu(self):
           print("Welcome to the best car rental in the world!")
           print("1. See available cars")
           print("2. Log in as customer")
           print("3. Log in as staff")
           print("Press q to quit")
           self.__action = input("Choose an option: ")
           if self.__action == "q" :
            	return
           elif self.__action == "1":
               self.seeAvailableCars()
           elif self.__action == "2":
               self.customerMenu()
           elif self.__action == "3":
               self.staffMenu()
           else :
            print("\nInvalid input, try again\n")
            self.mainMenu()

    def seeAvailableCars(self):
            print("\n\nHow would you like to sort the car list?")
            print("1. By price category")
            print("2. By manufacturer")
            print("3. By availability")
            print("Press q to quit and b to go back")
            self.__action = input("Choose an option: ").lower()
            if self.__action == "b" :
                self.staffMenu()
            elif self.__action == "q" :
                return

            elif self.__action == "1":
                self.printCarList("category")
            elif self.__action == "2":
                self.printCarList("manufacturer")
            elif self.__action == "3":
                self.printCarList("available")
            else :
                print("\nInvalid input, try again\n")
                self.seeAvailableCars()
    
    def printCarList(self, attribute):
        carList = self.__carService.getAndSortAvailableCars(attribute)
        counter = 0
        for car in carList:
            print(str(counter) + ". " + str(car))
            counter += 1

    def staffCarMenu(self):
            print("\n\n1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self.__action = input("Choose an option").lower()

            if self.__action == "b" :
                self.staffMenu()

            elif self.__action == "q" :
                return

            elif self.__action == "1":
                self.__carService.addCar()

            elif self.__action == "3":
                car = self.__carService.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.staffCarMenu()

    def customerCarMenu(self):
            print("\n\n1. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self.__action = input("Choose an option").lower()

            if self.__action == "b" :
                self.customerMenu()

            elif self.__action == "q" :
                return

            elif self.__action == "1":
                car = self.__carService.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.customerCarMenu()

    def staffMenu(self):
        print("\n\n1. Car management")
        print("2. Customer management") 
        print("3. Orders")
        print("Press b to return to the previous page")
        print("Press q to quit")
        self.__action = input("Choose an option").lower()

        if self.__action == "b" :
            self.mainMenu()
        elif self.__action == "q" :
            return
        elif self.__action == "1" :
            self.staffCarMenu()
        elif self.__action == "2" :
            self.staffCustomerMenu()
        elif self.__action == "3" :
            #self.staffOrderMenu()
            print('Ekkert komid')
        else :
            print("\nInvalid input, try again\n")
            self.staffMenu()

    def customerMenu(self):
        print("\n\n1. Car management")
        print("2. *** viljum vid hafa orders her ?******") 
        print("3. **************************************")
        print("Press b to return to the previous page")
        print("Press q to quit")
        self.__action = input("Choose an option").lower()

        if self.__action == "b" :
            self.mainMenu()
        elif self.__action == "q" :
            return
        elif self.__action == "1" :
            self.customerCarMenu()
        else :
            print("\nInvalid input, try again\n")
            self.staffMenu()

    def staffCustomerMenu(self):
            print("\n\n1. Add a customer")
            print("2. Remove a customer")
            print("3. List all customers")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self.__action = input("Choose an option").lower()

            if self.__action == "b" :
                self.staffMenu()

            elif self.__action == "q" :
                return

            elif self.__action == "1":
                self.__carService.addCar()

            elif self.__action == "3":
                car = self.__carService.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.staffCarMenu()