class Car:  
    def __init__(self, id = 0, category = "", manufacturer = "", model = "", year = "", mileage = "", seats = "", transmission = ""):
        self.__category = category
        self.__manufacturer = manufacturer
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__seats = seats
        self.__transmission = transmission
        self.__extras = []
        self.__id = 0
        self.__deleted = 0
        self.__rentHistory = []
        self.__available = 1

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.__id, self.__manufacturer, self.__model,
                                                   self.__category, self.__year, self. mileage,
                                                   self.__seats, self.__transmission, self.__available)

    def __repr__(self):
        return self.__str__()

#föllgit
    def deleteCar(self):
        self.__deleted = True

#Getterar
    @property
    def id(self):
        return self.__id

    @property
    def category(self):
        return self.__category

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def mileage(self):
        return self.__mileage

    @property
    def seats(self):
        return self.seats

    @property
    def transmission(self):
        return self.__transmission

    @property
    def extras(self):
        return self.__extras

    @property
    def history(self):
        return self.__rentHistory

    @property
    def available(self):
        return self.__available

    @property
    def deleted(self):
        return self.__deleted

#Setterar
    @id.setter
    def id(self, id):
        self.__id = id

    @category.setter
    def category(self, category):
        self.__category = category

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @model.setter
    def model(self, model):
        self.__model = model

    @year.setter
    def year(self, year):
        self.__year = year

    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage

    @seats.setter
    def seats(self, seats):
        self.__seats = seats

    @transmission.setter
    def transmission(self, transmission):
        self.__transmission = transmission

    @extras.setter 
    def extras(self, extras):
        self.__extras.append(extras)

    @history.setter 
    def history(self, history):
        self.__rentHistory.append(history)

    @available.setter
    def available(self, available):
        self.__available = available

    @deleted.setter
    def deleted(self, deleted):
        self.__deleted = int(deleted)