from ui.customerui import CustomerUI
from ui.staffui import StaffUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen


class MainUI:
   
    def __init__(self):
        self.__action = ""
    
    def mainMenu(self):
        action = ""
        while action != "q":
            clearScreen()
            print("Main Menu")
            if action == "rass":
                print("Finally you return to the main menu!!!")
                action = ""
            else:
                print("")
            print("These are your options:")
            print("")
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            action = input("Choose an option: ").lower()
            clearScreen()
            if action == "1":
                self.__customerui = CustomerUI()
                self.__customerui.seeAvailableCars()
                action = "rass"
            elif action == "2":
                self.__customerui = CustomerUI()
                self.__customerui.customerMenu()
                action = "rass"
            elif action == "3":
                self.__staffui = StaffUI()
                self.__staffui.logInAsStaff()
                action = "rass"