from models.creditcard import CreditCard
class User:

    def __init__(self, name = "", id = 0, socialNumber = "", driverLicense = "", address = "", phone = "", email = ""):
        self._name = name
        self._id = id
        self._socialNumber = socialNumber
        self._driverLicense = driverLicense
        self._address = address
        self._phone = phone
        self._email = email
        self._creditCard = CreditCard()
        self._rentHistory = []
        self._deleted = False
        self._employee = False
        self._pin = pin

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self._name, self._id, self._socialNumber, self._driverLicense, self._address, self._phone, self._email)


    def __repr__(self):
        return self.__str__()

    def deleteUser(self):
        self.__deleted = True

#Getterar
    @property
    def name(self):
        return self.__name

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