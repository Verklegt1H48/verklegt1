from ui.customerui import CustomerUI
from ui.staffui import StaffUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen


class MainUI:
   
    def __init__(self):
        self.__action = ""
    
    # Interface for the main menu
    def mainMenu(self):
        action = ""
        while action != "q":
            login = False
            clearScreen()
            print("Main Menu")
            if action == "return":
                print("If you were logged in, you have been logged out.")
                action = ""
            else:
                print("")
            print("These are your options:")
            print("")
            print("1. Browse cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("q. Exit program")
            if action != "":
                print("Invalid input! Please try again.")
            else:
                print("")
            action = input("Choose an option: ").lower()
            
            clearScreen()
            if action == "1":
                self.__customerui = CustomerUI()
                login  = self.__customerui.seeAvailableCars()
                action = ""
            if action == "2" or login is True:
                self.__customerui = CustomerUI()
                self.__customerui.customerMenu()
                action = "return"
            if action == "3":
                self.__staffui = StaffUI()
                self.__staffui.logInAsStaff()
                action = "return"