from models.car import Car
from services.carservice import CarService
from models.user import User

class CustomerUI:
    
    def __init__(self):
        self.__car_service = CarService()

    def mainMenu(self):
        newCar = Car()
        action = ""
        while(action != "q"):
            print("1. Add a car")
            print("2. List all car")
            print("Press q to quit")

            action = input("Choose an option").lower()

            if action == "1":
                newCar._category = input("Category: ")
                newCar._manufacturer = input("Manufacturer: ")
                newCar._model = input("Model: ")
                newCar._year = input("Year: ")
                newCar._milage = input("Milage: ")
                newCar._seats = input("Seats: ")
                newCar._transmission = input("Transmission: ")
                newCar._extras = input("Extras: ")
                newCar._id = input("Id: ")
                self.__car_service.addCar(newCar)

            elif action == "2":
                car = self.__car_service.getCar()
                print(car)        