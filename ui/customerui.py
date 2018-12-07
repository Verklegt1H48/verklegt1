from models.car import Car
from services.carservice import CarService
from services.orderservice import OrderService
from models.user import User
from datetime import datetime
class CustomerUI:
    
    def __init__(self):
        self.__carService = CarService()
        self.__orderService = OrderService()
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
                self.mainMenu()
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
        counter = 1
        for car in carList:
            print(str(counter) + ". " + str(car))
            counter += 1

        self.__action = input("\nPlease select the car you wish to book: ").lower()
        print("Press q to quit and b to go back")
        if self.__action == "b" :
            self.seeAvailableCars()
        elif self.__action == "q" :
            return
        elif int(self.__action) >= counter:
            print("\nInvalid input, try again\n")
            self.seeAvailableCars()
        else :
            carToOrder = carList[int(self.__action) - 1]
            del carList
            print("\nYou chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
            print("Current price is " + carToOrder.price + " isk per day")
            currPrice = self.addInsurance(carToOrder)
            daysToRent = self.obtainPickupAndReturnDate()
            finalPrice = int(daysToRent.days) * currPrice #LAGA
            print("Your final price is " + str(finalPrice))
            

            
    
    def addInsurance(self, carToOrder):
            
        print("Press q to quit and b to go back")
        if self.__action == "b" :
            self.seeAvailableCars()
        elif self.__action == "q" :
            return
        
        carInsurance = str(int(int(carToOrder.price) / 10))
        self.__action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")
        if self.__action == "y":    
            totalPrice = str(int(carInsurance) + int(carToOrder.price))
            print("Your total price per day is " + totalPrice + " isk")
            return totalPrice
        elif self.__action == "n":
            print("Your total price per day is " + carToOrder.price + " isk")
            return carToOrder.price
        else:
            print("\nInvalid input, try again\n")
            self.addInsurance(carToOrder)


    def obtainPickupAndReturnDate(self):
        pickupDate = input("When will you pick up your car? (dd/mm/yy): ")
        pickupCar = datetime.strptime(pickupDate, "%d/%m/%y")
        returnDate = input("When will you return the car? (dd/mm/yy): ")
        returnCar = datetime.strptime(returnDate, "%d/%m/%y")
        return returnCar - pickupCar


                
    def staffCarMenu(self):
            print("\n\n1. Add a car")
            print("2. Remove a car")
            print("3. List all cars")
            print("Press b to return to the previous page")
            print("Press q to quit")
            self.__action = input("Choose an option: ").lower()

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
            self.__action = input("Choose an option: ").lower()

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
        self.__action = input("Choose an option: ").lower()

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

    def orderMenu(self):
        print("\n\n1. Orders")
        print("2. Confirmed orders") 
        print("3. Unconfirmed orders")
        print("Press b to return to the previous page")
        print("Press q to quit")

        if self.__action == "b" :
            self.staffMenu()
        elif self.__action == "q" :
            return
        elif self.__action == "1" :
            self.staffCarMenu()
        elif self.__action == "2" :
            self.__orderService.getOrdersByStatus(1)
        elif self.__action == "3" :
            self.__orderService.getOrdersByStatus(0)
        else :
            print("\nInvalid input, try again\n")
            self.orderMenu()

    def customerMenu(self):
        print("\n\n1. Car management")
        print("2. *** viljum vid hafa orders her ?******") 
        print("3. **************************************")
        print("Press b to return to the previous page")
        print("Press q to quit")
        self.__action = input("Choose an option: ").lower()

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
            self.__action = input("Choose an option: ").lower()

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