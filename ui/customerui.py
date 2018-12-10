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
            action = ""
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
                    if(daysToRent != ""):
                        finalPrice = int(daysToRent.days) * int(currPrice)
                        print("Your final price is " + str(finalPrice))
                        exit("Lengra er eg ekki kominn med thessa utfaerslu")


    def addInsurance(self, carToOrder):
            
        action = ""
        while action != "b":
            print("Press q to quit and b to go back")  
            carInsurance = str(int(int(carToOrder.price) / 10))
            if action != "":
                print("Invalid input, try again")
            action = input("Would you like to add insurance for an additional " + carInsurance + " isk per day?(y/n): ")
            clearScreen()
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
                    


    def obtainPickupAndReturnDate(self):
        action = ""
        while action != "b":
            action = input("When will you pick up your car? (dd/mm/yy): ")
            if action == "b" :
                return ""
            elif action == "q" :
                exit(1)
            try:
                pickupCar = datetime.strptime(action, "%d/%m/%y")
                if pickupCar > datetime.today():
                    break
                else:
                    raise Exception
            except:
                clearScreen()
                print("Invalid date input!")
                
        action = ""
        while action != "b":
            action = input("When will you return the car? (dd/mm/yy): ")
            if action == "b" :
                return ""
            elif action == "q" :
                exit(1)
            try:
                returnCar = datetime.strptime(action, "%d/%m/%y")
                if returnCar > pickupCar:
                    break
                else:
                    raise Exception
            except:
                clearScreen()
                print("When will you pick up your car? (dd/mm/yy): " + str(pickupCar.day) +\
                "/" + str(pickupCar.month) + "/" + str(pickupCar.year - 2000))
                print("Invalid date input!")
        return returnCar - pickupCar


    def customerMenu(self):
        print("\n\n1. Car management")
        print("2. *** viljum vid hafa orders her ?******") 
        print("3. **************************************")
        print("4. Order List")
        print("5. See car history")
        print("Press b to return to the previous page")
        print("Press q to quit")
        action = input("Choose an option: ").lower()

        #if action == "b" :
         #   self.__mainui.mainMenu()
        if action == "q" :
            return
        elif action == "1" :
            self.seeAvailableCars()
        elif action == "4" :
            orders = self.__orderService.getOrderList()
            print(orders)
        elif action == "5" :
            id = input("Enter Car Id: " )
            self.__carService.getCarHistory(int(id))

        else :
            print("\nInvalid input, try again\n")
            self.customerMenu()

    
