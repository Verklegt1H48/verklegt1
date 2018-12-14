from helperfunctions.helpers import clearScreen
import getpass


def printHeader(header):
    if header == "welcome":
        print(welcomeScreen)
        getpass.getpass("")
    elif header == "carSelect":
        print(carSelectHeader)
    elif header == "orderSelect":
        print(orderSelectHeader)
    elif header == "userSelect":
        print(userSelectHeader)
    elif header == "staffSelect":
        print(staffSelectHeader)

# ASCII art from https://www.asciiart.eu/vehicles/cars

welcomeScreen = (r"""

                       ____________________
                     //|           |        \
                   //  |           |          \
      ___________//____|___________|__________()\__________________
    /__________________|_=_________|_=___________|_________________{}
    [           ______ |           | .           | ==  ______      { }
  __[__        /##  ##\|           |             |    /##  ##\    _{# }_
 {_____)______|##    ##|___________|_____________|___|##    ##|__(______}
                ##__##                                 ##__##

                        WELCOME TO SANTAS CAR RENTAL
                       PLEASE PRESS ENTER TO CONTINUE
-------------------------------------------------------------------------- """)

carSelectHeader = ("{:5}{:10}{:7}{:15}{:15}{:7}{:10}{:8}{:15}{:10}".format("ID", "Category", "Price",
                                                                           "Manufacturer", "Model", "Year",
                                                                           "Mileage", "Seats", "Transmission",
                                                                           "Extras"))

orderSelectHeader = ("{:8}{:8}{:10}{:7}{:16}{:15}{:15}".format("Number", "UserID", "Category",
                                                               "CarID", "Payment Method",
                                                               "Pick Up Date", "Return Date"))

userSelectHeader = ("{:25}{:5}{:12}{:15}{:15}{:15}{:15}".format("Name", "ID", "Social", "License nr.",
                                                                "Address", "Phone", "Email"))

staffSelectHeader = ("{:25}{:5}{:16}".format("Name", "ID", "Social"))
