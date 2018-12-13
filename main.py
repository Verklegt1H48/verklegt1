from ui.mainui import MainUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen, resizeWindow


def main():
    clearScreen()
    printHeader("welcome")
    resizeWindow()
    ui = MainUI()
    ui.mainMenu()
main()
