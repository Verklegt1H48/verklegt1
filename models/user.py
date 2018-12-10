class User:

    def __init__(self, name = "", id = 0, socialNumber = "", driverLicense = "", address = "", phone = "", email = ""):
        self.__name = name
        self.__username = ""
        self.__password = ""
        self.__id = id
        self.__socialNumber = socialNumber
        self.__driverLicense = driverLicense
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__nameOnCard = ""
        self.__number = ""
        self.__cvv = ""
        self.__expMonth = ""
        self.__expYear = ""
        self.__rentHistory = []
        self.__deleted = False
        self.__employee = False


    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.__name, self.__id, self.__socialNumber, self.__driverLicense, self.__address, self.__phone, self.__email)


    def __repr__(self):
        return self.__str__()

    def deleteUser(self):
        self.__deleted = True

#Getterar
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

#Setterar
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