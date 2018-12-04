from models.car import Car

class CarRepository:

    def __init__(self):
        self.__car = []

    def addCar(self, car):
        with open("./data/cars.txt", "a+") as cars_file:
            _category = car.get_category()
            _manufacturer = car.get_manufacturer()
            _model = car.get_model()
            _year = car.get_year()
            _milage = car.get_milage()
            _seats = car.get_seats()
            _transmission = car.get_transmission()
            _extras = car.get_extras()
            _id = car.get_id()
            cars_file.write("{},{},{},{},{},{},{},{},{}\n".format(_category, _manufacturer, _model, _year,
            _milage, _seats, _transmission, _extras, _id))

    def getCar(self, Car):
        if self.__car == []:
            with open("./data/cars.txt","r") as car_file:
                for line in car_file.readlines():
                    category, manufacturer, model, year, milage, seats, transmission, extras, id = line.strip().split(",")
                    new_car = Car(category, manufacturer, model, year, milage, seats, transmission, extras, id)
                    self.__car.append(new_car)

                return self.__car
   # def getCarList(self):

       # self._category = ""
       # self._manufacturer = ""
       # self._model = ""
       # self._year = 0
       # self._milage = 0
       # self._seats = 0
       # self._transmission = ""
       # self._extras = []
       # self._id = 0
       # self._deleted = False
       # self._rentHistory = []
       # self._available = True