from models.car import Car
from services.carservice import CarService
from services.orderservice import OrderService
from models.user import User
from datetime import datetime


class CustomerUI:
    
    def __init__(self):
        self.__carService = CarService()
        self.__orderService = OrderService()
        #self.__mainui = MainUI()
        self.__action = ""

    def seeAvailableCars(self):
        print("\n\nHow would you like to sort the car list?")
        print("1. By price category")
        print("2. By manufacturer")
        print("3. By availability")
        print("Press q to quit and b to go back")
        self.__action = input("Choose an option: ").lower()
        #if self.__action == "b" :
            #self.__mainui.mainMenu()
        if self.__action == "q" :
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
            print("You chose the " + str(carToOrder.year) + " " + carToOrder.manufacturer + " " + carToOrder.model)
            print("Current price is " + carToOrder.price + " isk per day")
            currPrice = self.addInsurance(carToOrder)
            daysToRent = self.obtainPickupAndReturnDate()
            finalPrice = int(daysToRent.days) * int(currPrice)
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
        #ljotasti kodi ever
        isValid = False
        while not isValid:
            self.__action = input("When will you pick up your car? (dd/mm/yy): ")
            if self.__action == "b" :
                self.seeAvailableCars()
            elif self.__action == "q" :
                return
            try:
                pickupCar = datetime.strptime(self.__action, "%d/%m/%y")
                if pickupCar > datetime.today():
                    isValid = True
                else:
                    raise Exception
            except:
                print("Invalid date input!")
                
        isValid = False
        while not isValid:
            self.__action = input("When will you return the car? (dd/mm/yy): ")
            if self.__action == "b" :
                self.seeAvailableCars()
            elif self.__action == "q" :
                return
            try:
                returnCar = datetime.strptime(self.__action, "%d/%m/%y")
                if returnCar > pickupCar:
                    isValid = True
                else:
                    raise Exception
            except:
                print("Invalid date input!")
        return returnCar - pickupCar


    def customerMenu(self):
        print("\n\n1. Car management")
        print("2. *** viljum vid hafa orders her ?******") 
        print("3. **************************************")
        print("Press b to return to the previous page")
        print("Press q to quit")
        self.__action = input("Choose an option: ").lower()

        #if self.__action == "b" :
         #   self.__mainui.mainMenu()
        if self.__action == "q" :
            return
        elif self.__action == "1" :
            self.seeAvailableCars()
        else :
            print("\nInvalid input, try again\n")
            self.customerMenu()

    