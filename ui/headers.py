from helperfunctions.helpers import clearScreen

def printHeader(header):
    if header == "login":
        print(loginHeader)
    elif header == "main":
        print(mainHeader)
    elif header == "carSelect":
        print(carSelectHeader)
    elif header == "orderSelect":
        print(orderSelectHeader)


loginHeader = "rass"

mainHeader = (r"""

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

carSelectHeader = ("{:10}{:10}{:7}{:15}{:10}{:7}{:10}{:8}{:15}{:10}".format("Number","Category","Price","Manufacturer",
                                                                            "Model","Year", "Mileage","Seats",
                                                                            "Transmission","Extras"))

orderSelectHeader = ("{:8}{:8}{:10}{:7}{:16}{:15}{:15}".format("Number","UserID","Category","CarID","Payment Method",
                             "Pick Up Date","Return Date"))