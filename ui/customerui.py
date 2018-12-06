from models.car import Car
from services.carservice import CarService
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__carservice = CarService()
        self._action = ""
    def mainMenu(self):

        print("\n\nWelcome to the best car rental in the world!")
        print("1. See available cars")
        print("2. Log in as customer")
        print("3. Log in as staff")
        print("Press q to quit any time")
        self._action = input("Choose an option: ")

        if self._action == "q" :
            return

        elif self._action == "1":
            self.customerCarMenu()

        elif self._action == "2":
            self.customerMenu()
        
        elif self._action == "3":
            self.staffMenu()
        else :
            print("\nInvalid input, try again\n")
            self.mainMenu()


    def staffCarMenu(self):
            print("\n\n1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self._action = input("Choose an option: ").lower()

            if self._action == "b" :
                self.staffMenu()

            elif self._action == "q" :
                return

            elif self._action == "1":
                newCar = Car()
                newCar._category =     input("Category: ")
                newCar._manufacturer = input("Manufacturer: ")
                newCar._model =        input("Model: ")
                newCar._year =         input("Year: ")
                newCar._milage =       input("Milage: ")
                newCar._seats =        input("Seats: ")
                newCar._transmission = input("Transmission: ")
                newCar._extras =       input("Extras: ")
                newCar._id =           input("Id: ")
                self.__carservice.addCar(newCar)

            elif self._action == "3":
                car = self.__carservice.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.staffCarMenu()

    def customerCarMenu(self):
            print("\n\n1. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self._action = input("Choose an option: ").lower()

            if self._action == "b" :
                self.customerMenu()

            elif self._action == "q" :
                return

            elif self._action == "1":
                car = self.__carservice.getCarList()
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
        self._action = input("Choose an option: ").lower()

        if self._action == "b" :
            self.mainMenu()
        elif self._action == "q" :
            return
        elif self._action == "1" :
            self.staffCarMenu()
        elif self._action == "2" :
            self.staffCustomerMenu()
        elif self._action == "3" :
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
        self._action = input("Choose an option: ").lower()

        if self._action == "b" :
            self.mainMenu()
        elif self._action == "q" :
            return
        elif self._action == "1" :
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
            self._action = input("Choose an option: ").lower()

            if self._action == "b" :
                self.staffMenu()

            elif self._action == "q" :
                return

            elif self._action == "1":
                self.__carservice.addCar()

            elif self._action == "3":
                car = self.__carservice.getCarList()
                print(car)
            
            else :
                print("\nInvalid input, try again\n")
                self.staffCarMenu()