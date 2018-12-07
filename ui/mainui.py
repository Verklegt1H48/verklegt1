from ui.customerui import CustomerUI
from ui.staffui import StaffUI


class MainUI:
   
    def __init__(self):
        self.__staffui = StaffUI()
        self.__customerui = CustomerUI()
        self.__action = ""
    
    def mainMenu(self):
            print("\n\nWelcome to the best car rental in the world!")
            print("1. See available cars")
            print("2. Log in as customer")
            print("3. Log in as staff")
            print("Press q to quit")
            self.__action = input("Choose an option: ")
            if self.__action == "q" :
             	return
            elif self.__action == "1":
                self.__customerui.seeAvailableCars()
            elif self.__action == "2":
                self.__customerui.customerMenu()
            elif self.__action == "3":
                self.__staffui.staffMenu()
            else :
             print("\nInvalid input, try again\n")
             self.mainMenu()