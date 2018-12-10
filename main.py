from ui.mainui import MainUI
from ui.headers import printHeader
from helperfunctions.helpers import clearScreen
from repositories.carrepository import CarRepository


def main():
    printHeader("main")
    input("")
    ui = MainUI()
    ui.mainMenu()

main()