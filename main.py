from repositories.carrepository import CarRepository
from operator import itemgetter,attrgetter
from helpers.helpers import clearScreen

def main():
    carRepo = CarRepository()
    cars = carRepo.getCarList()
    sortedCars = sorted(cars, key=attrgetter('id'))
        
main()

