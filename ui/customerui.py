from models.car import Car
from services.carservice import CarService
from services.orderservice import OrderService
from models.user import User
from datetime import datetime
from helperfunctions.helpers import clearScreen


class CustomerUI:
    
    def __init__(self):
        self.__carService = CarService()
        self.__orderService = OrderService()

    def seeAvailableCars(self):
        action = ""
        while action != "b":
            action = ""
            print("Press q to quit and b to go back")
            print("How would you like to sort the car list?")
            print("1. By price category")
            print("2. By manufacturer")
            print("3. By availability")
            if action != "":
                print("Invalid input, try again\n")
            action = input("Choose an option: ").lower()
            clearScreen()
            if action == "q":
                exit(1)
            elif action == "1":
                self.printCarList("category")
            elif action == "2":
                self.printCarList("manufacturer")
            elif action == "3":
                self.printCarList("available") 
                
    
    def printCarList(self, attribute):
        action = ""
        while action != "b":

            carList = self.__carService.getAndSortAvailableCars(attribute)
            counter = 1
            for car in carList:
                print(str(counter) + ". " + str(car))
                counter += 1
            if action != "":
                print("Invalid input, try again")
            action = input("Please select the car you wish to book: ").lower()
            clearScreen()
            if action == "q" :
                exit(1)
            elif action == "b":
                pass
            elif action.isdecimal() == False:
                pass
            elif int(action) >= counter:
                pass
            elif int(action) <= 0:
                pass
            else :
                carToOrder = carList[int(action) - 1]
                del carList
                print("You chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
                print("Current price is " + carToOrder.price + " isk per day")
                currPrice = ""
                currPrice = self.addInsurance(carToOrder)
                if(currPrice != ""):
                    daysToRent = self.obtainPickupAndReturnDate()
                    finalPrice = int(daysToRent.days) * int(currPrice)
                    print("Your final price is " + str(finalPrice))
                    exit("Lengra er eg ekki kominn med thessa utfaerslu vinur")


    def addInsurance(self, carToOrder):
            
        action = ""
        while action != "b":
            action = ""
            print("Press q to quit and b to go back")  
            carInsurance = str(int(int(carToOrder.price) / 10))
            if action != "":
                print("Invalid input, try again")
            action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")
            if action == "y":    
                totalPrice = str(int(carInsurance) + int(carToOrder.price))
                print("Your total price per day is " + totalPrice + " isk")
                return totalPrice
            elif action == "n":
                print("Your total price per day is " + carToOrder.price + " isk")
                return carToOrder.price
            return ""
                    


    def obtainPickupAndReturnDate(self):
        #ljotasti kodi ever
        isValid = False
        while not isValid:
            action = input("When will you pick up your car? (dd/mm/yy): ")
            if action == "b" :
                self.seeAvailableCars()
            elif action == "q" :
                return
            try:
                pickupCar = datetime.strptime(action, "%d/%m/%y")
                if pickupCar > datetime.today():
                    isValid = True
                else:
                    raise Exception
            except:
                print("Invalid date input!")
                
        isValid = False
        while not isValid:
            action = input("When will you return the car? (dd/mm/yy): ")
            if action == "b" :
                self.seeAvailableCars()
            elif action == "q" :
                return
            try:
                returnCar = datetime.strptime(action, "%d/%m/%y")
                if returnCar > pickupCar:
                    isValid = True
                else:
                    raise Exception
            except:
                print("Invalid date input!")
        return returnCar - pickupCar

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
        print("3. Return a car")
        print("Press b to return to the previous page")
        print("Press q to quit")
        action = input("Choose an option: ").lower()

        #if action == "b" :
         #   self.__mainui.mainMenu()
        if action == "q" :
            return
        elif action == "1" :
            self.seeAvailableCars()
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