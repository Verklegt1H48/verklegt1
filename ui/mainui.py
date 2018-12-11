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
            clearScreen()
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("Press q to quit")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            clearScreen()
            if action == "1":
                self.__customerui.seeAvailableCars()
                action = ""
            elif action == "2":
                self.__customerui.customerMenu()
                action = ""
            elif action == "3":
                self.__staffui.logInAsStaff()
                action = ""