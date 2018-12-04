class Order:


    #def __init__(self):
    #    self._id = 0 #Utfaera seinna
    #    self._userId = 0
    #    self._carCategory = ""
    #    self._carId = 0
    #    self._payMethod = ""
    #    self._status = False
    #    self._deleted = False 

    def __init__(self,id=0, userId=0, carCatagory="", carId=0, payMethod="", status=False, deleted=False):
        self._id = id
        self._userId = userId
        self._carCategory = carCatagory
        self._carId = carId
        self._payMethod = payMethod
        self._status = status
        self._deleted = deleted

    def __str__(self):
        "{},{},{},{},{},{}".format(self._id, self._userId, self._carCategory,\
        self._carId, self._payMethod, self._status,)

    def __repr__(self):
        return self.__str__()

#Getters
    @property
    def carId(self):
        return self._carId

    @property
    def status(self):
        return self._status

    @property
    def deleted(self):
        return self._deleted
#Setters
    @carId.setter
    def carId(self, value):
        self._carId = value

    @status.setter
    def status(self, value):
        self._status = value

    @deleted.setter
    def deleted(self, value):
        self._deleted = value
    


     
