class Car:
    def __init__(self,id,car,category,manufacturer,model,year,milage,seats,transmission,extras):
        #self.id = len(getCarList()) + 1
        self.deleted = False
        self.rentHistory = []
    @property
    def id(self):
        return self.id
    @property
    def category(self):
        return self.category
    @property
    def manufacturer(self):
        return self.manufacturer
    @property
    def model(self):
        return self.model
    @property
    def year(self):
        return self.year
    @property
    def mileage(self):
        return self.mileage
    @property
    def seats(self):
        return self.seats
    @property
    def transmission(self):
        return self.transmission
    @property
    def extras(self):
        return self.extras
    @property
    def history(self):
        return self.history
    @category.setter
    def category(self, category):
        self.category = category
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    @model.setter
    def model(self, model):
        self.model = model
    @year.setter
    def year(self, year):
        self.year = year
    @mileage.setter
    def mileage(self, mileage):
        self.mileage = mileage
    @seats.setter
    def seats(self, seats):
        self.seats = seats
    @transmission.setter
    def transmission(self, transmission):
        self.transmission = transmission
    @extras.setter 
    def extras(self, extras):
        self.extras = extras
    @history.setter 
    def history(self, history):
        appendself.history = extras