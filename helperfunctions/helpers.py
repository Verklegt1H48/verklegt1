#import info about system
from os import system, name

#define a function to clear the screen
def clearScreen():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac and linux
    else:
        _ = system('clear')

def resizeWindow():
    #windows
    if name == 'nt':
        _ = system("mode CON: COLS=150")
    #mac and linux
    else:
        _ = system("printf '\\e[9;1t'")

def printList(self, list):
    for object in list:
        print(object)

def getHistory(orders, id, carOrUser):
        if carOrUser == "car":
            form = "UserID"
        else:
            form = "CarID"
        print("->Print order history for {} with ID: \"{}\"".format(carOrUser, id))
        print("")
        print("These are the history items for this {}:".format(carOrUser))
        print("{:10}{:15}{:15}".format(form, "Pick Up date", "Return date"))
        if carOrUser == "car":
            for order in orders:
                if str(order.carId) == str(id):
                    print("{:10}{:15}{:15}".format(str(order.userId), order.pickUpDate, order.returnDate))
        else:
            for order in orders:
                if str(order.carId) == str(id):
                    print("{:10}{:15}{:15}".format(str(order.carId), order.pickUpDate, order.returnDate))
        print("")
        input("Press enter to return ")