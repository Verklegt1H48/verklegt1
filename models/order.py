class Order:

    def __init__(self):
        self._id = 0 #Utfaera seinna
        self._userId = 0
        self._carCategory = ""
        self._carId = 0
        self._payMethod = ""
        self._status = False
        self._deleted = False

    @property
    def carId(self):
        return self._carId

    @property
    def status(self):
        return self._status

    @property
    def deleted(self):
        return self._deleted

    @carId.setter
    def carId(self, value):
        self._carId = value

    @status.setter
    def status(self, value):
        self._status = value

    @deleted.setter
    def deleted(self, value):
        self._deleted = value
    


     
