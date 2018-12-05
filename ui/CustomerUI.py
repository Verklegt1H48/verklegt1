from services.carservice import CarService
from models.car import Car

class CustomerUI:
    
    def __init__(self):
        self.__car_service = CarService()

    def mainMenu(self):

        action = ""
        while(action != "q"):
            print("1. Add a car")
            print("2. List all car")
            print("Press q to quit")

            action = input("Choose an option").lower()

            if action == "1":
                category = input("Category: ")
                manufacturer = input("Manufacturer: ")
                model = input("Model: ")
                year = input("Year: ")
                milage = input("Milage: ")
                seats = input("Seats: ")
                transmission = input("Transmission: ")
                extras = input("Extras: ")
                id = input("Id: ")
                new_car = Car(1,2,3,4,5,6,7,8)
                self.__car_service.addCar(new_car)

            elif action == "2":
                Car = self.__car_service.getCar()
                print(Car)        