from ui.customerui import CustomerUI
from ui.staffui import StaffUI
from helperfunctions.helpers import clearScreen


class MainUI:
   
    def __init__(self):
        self.__staffui = StaffUI()
        self.__customerui = CustomerUI()
        self.__action = ""
    
    def mainMenu(self):
        action = ""
        while action != "q":
            print("Welcome to the best car rental in the world!")
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("Press q to quit")
            action = input("Choose an option: ")
            clearScreen()
            if action == "1":
                self.__customerui.seeAvailableCars()
            elif action == "2":
                self.__customerui.customerMenu()
            elif action == "3":
                self.__staffui.staffMenu()
            else:
                print("Invalid input, try again")
                print("Concentrate, buddy!\n")