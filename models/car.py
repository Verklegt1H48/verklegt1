class Car:
    def __init__(self):
        self._category = ""
        self._manufacturer = ""
        self._model = ""
        self._year = 0
        self._milage = 0
        self._seats = 0
        self._transmission = ""
        self._extras = []
        self._id = 0
        self._deleted = False
        self._rentHistory = []
        self._available = True

#föll
    def deleteCar(self):
        self._deleted = True

#Getterar
    @property
    def id(self):
        return self._id

    @property
    def category(self):
        return self._category

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def mileage(self):
        return self._mileage

    @property
    def seats(self):
        return self.seats

    @property
    def transmission(self):
        return self._transmission

    @property
    def extras(self):
        return self._extras

    @property
    def history(self):
        return self._history
    @property
    def available(self):
        return self._available


#Setterar

    @category.setter
    def category(self, category):
        self._category = category

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    @model.setter
    def model(self, model):
        self._model = model

    @year.setter
    def year(self, year):
        self._year = year

    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    @seats.setter
    def seats(self, seats):
        self._seats = seats

    @transmission.setter
    def transmission(self, transmission):
        self._transmission = transmission

    @extras.setter 
    def extras(self, extras):
        self._extras.append(extras)

    @history.setter 
    def history(self, history):
        self._rentHistory.append(history)

    @available.setter
    def available(self, available):
        self._available = available
