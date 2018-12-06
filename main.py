from repositories.carrepository import CarRepository
from operator import itemgetter,attrgetter
from helpers.helpers import clearScreen

def main():
    carRepo = CarRepository()
    cars = carRepo.getCars()
    sortedCars = sorted(cars, key=attrgetter('id'))
    
    #clearScreen()
    #for car in sortedCars:
    #    print(car.extras[0].strip("[']",))
        

main()