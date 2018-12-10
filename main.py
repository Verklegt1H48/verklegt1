
from ui.mainui import MainUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen


def main():
    printHeader("main")
    input("")
    ui = MainUI()
    ui.mainMenu()
 
main()