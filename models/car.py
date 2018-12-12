class Car:

    def __init__(self, id = 0, category = "", manufacturer = "", model = "", year = "", mileage = "",
                 seats = "",transmission = "", price = ""):
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
        self.__price = 0

    def __repr__(self):
        return "{:10}{:7}{:15}{:15}{:7}{:10}{:8}{:15}{:10}".format(self.__category, str(self.__price), self.__manufacturer,
                                                                   str(self.__model), str(self.__year), str(self.__mileage),
                                                                   str(self.__seats), self.__transmission,
                                                                   str(self.__extras).strip("[']").replace("', '", ", "))

#föllgit
    def deleteCar(self):
        self.__deleted = True

#Getterar
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return int(self.__price)

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
        return self.__seats

    @property
    def transmission(self):
        return self.__transmission

    @property
    def extras(self):
        return self.__extras

    @property
    def rentHistory(self):
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
        self.__id = int(id)

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
        self.__seats = int(seats)

    @transmission.setter
    def transmission(self, transmission):
        self.__transmission = transmission

    @extras.setter 
    def extras(self, extras):
        self.__extras.append(extras)

    @rentHistory.setter 
    def rentHistory(self, rentHistory):
        self.__rentHistory.append(rentHistory)

    @available.setter
    def available(self, available):
        self.__available = int(available)

    @deleted.setter
    def deleted(self, deleted):
        self.__deleted = int(deleted)
    
    @price.setter
    def price(self, price):
        self.__price = price