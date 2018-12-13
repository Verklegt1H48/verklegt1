class User:

    def __init__(self, name = "", socialNumber = "", employee = "", pin = "", password = "", id = 0, driverLicense = "",
                address = "", phone = "", email = "", nameOnCard = "", number = "", cvv = "", expMonth = "", expYear = "" ):
        self.__name = name
        self.__password = password
        self.__id = id
        self.__socialNumber = socialNumber
        self.__driverLicense = driverLicense
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__nameOnCard = nameOnCard
        self.__number = number
        self.__cvv = cvv
        self.__expMonth = expMonth
        self.__expYear = expYear
        self.__rentHistory = []
        self.__deleted = 0
        self.__employee = employee
        self.__pin = pin

    def __repr__(self):
        return "{:25}{:5}{:12}{:15}{:15}{:15}{:15}".format(str(self.__name), str(self.__id), str(self.__socialNumber), 
                                                        str(self.__driverLicense), str(self.__address), str(self.__phone), 
                                                        str(self.__email))

#Getters

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    @property
    def id(self):
        return self.__id

    @property
    def socialNumber(self):
        return self.__socialNumber

    @property
    def driverLicense(self):
        return self.__driverLicense

    @property
    def nameOnCard(self):
        return self.__nameOnCard

    @property
    def number(self):
        return self.__number

    @property
    def cvv(self):
        return self.__cvv

    @property
    def expMonth(self):
        return self.__expMonth

    @property
    def expYear(self):
        return self.__expYear

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @property
    def employee(self):
        return self.__employee

    @property
    def pin(self):
        return self.__pin

    @property
    def rentHistory(self):
        return self.__rentHistory

    @property
    def deleted(self):
        return self.__deleted

#Setters

    @name.setter
    def name(self, value):
        self.__name = value
    @password.setter
    def password(self, value):
        self.__password = value

    @id.setter
    def id(self, value):
        self.__id = value

    @socialNumber.setter
    def socialNumber(self, value):
        self.__socialNumber = value
    
    @driverLicense.setter
    def driverLicense(self, value):
        self.__driverLicense = value

    @address.setter
    def address(self, value):
        self.__address = value

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @email.setter
    def email(self, value):
        self.__email = value
    
    @employee.setter
    def employee(self, value):
        self.__employee = value

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @rentHistory.setter
    def rentHistory(self, value):
        self.__rentHistory = value

    @deleted.setter
    def deleted(self, value):
        self.__deleted = value

    @nameOnCard.setter
    def nameOnCard(self, value):
        self.__nameOnCard = value
    
    @number.setter
    def number(self, value):
        self.__number = value

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @expMonth.setter
    def expMonth(self, value):
        self.__expMonth = value

    @expYear.setter
    def expYear(self, value):
        self.__expYear = value