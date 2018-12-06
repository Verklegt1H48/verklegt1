from ui.customerui import CustomerUI
from helpers.helpers import clearScreen


def main():
    carRepo = CarRepository()
    cars = carRepo.getCarList()
    sortedCars = sorted(cars, key=attrgetter('id'))
        
main()


ui = CustomerUI()

ui.mainMenu()

