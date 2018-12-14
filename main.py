from ui.mainui import MainUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen


def main():
    clearScreen()
    printHeader("welcome")
    ui = MainUI()
    ui.mainMenu()

main()
