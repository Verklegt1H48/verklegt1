from helperfunctions.helpers import clearScreen

def printHeader(header):
    clearScreen()
    if header == "loginHeader":
        print(loginHeader)
    if header == "mainHeader":
        print(mainHeader)


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

                        WELCOME TO SATANS CAR RENTAL
                          PRESS ENTER TO CONTINUE
-------------------------------------------------------------------------- """)