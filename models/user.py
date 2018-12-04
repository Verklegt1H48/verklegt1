from creditcard import CreditCard
class User:

    def __init__(self):
        self._name = ""
        self._id = ""
        self._socialNumber = ""
        self._driverLicense = ""
        self._address = ""
        self._phone = ""
        self._email = ""
        self._creditCard = CreditCard()
        self._rentHistory = []
        self._deleted = False
        self._employee = False
        self._pin = ""


    def deleteUser(self):
        self._deleted = True

    
#Getterar
    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def socialNumber(self):
        return self._socialNumber

    @property
    def driverLicense(self):
        return self._driverLicense

    @property
    def address(self):
        return self._address

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def employee(self):
        return self._employee

    @property
    def pin(self):
        return self._pin

    @property
    def rentHistory(self):
        return self._rentHistory

    @property
    def deleted(self):
        return self._deleted

#Setterar
    @name.setter
    def name(self, value):
        self._name = value

    @id.setter
    def id(self, value):
        self._id = value = value

    @socialNumber.setter
    def socialNumber(self, value):
        self._socialNumber = value
    
    @driverLicense.setter
    def driverLicense(self, value):
        self._driverLicense = value

    @address.setter
    def address(self, value):
        self._address = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    @email.setter
    def email(self, value):
        self._email = value
    

    @employee.setter
    def employee(self, value):
        self._employee = value

    @pin.setter
    def pin(self, value):
        self._pin = value

    @rentHistory.setter
    def rentHistory(self, value):
        self._rentHistory = value

    @deleted.setter
    def deleted(self, value):
        self._deleted = value