class Order:

    def __init__(self,id = 0, userId = 0, carCategory = "", carId = 0, payMethod = "", status = False, deleted = False, pickUpData = "", returnDate = ""):
        self.__id = id
        self.__userId = userId
        self.__carCategory = carCategory
        self.__carId = carId
        self.__payMethod = payMethod
        self.__status = status
        self.__deleted = deleted
        self.__pickUpDate = pickUpData
        self.__returnDate = returnDate

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__id, self.__userId, self.__carCategory,\
        self.__carId, self.__pickUpDate, self.__returnDate, self.__payMethod, self.__status,)

    def __repr__(self):
        return self.__str__()

#Getters
    @property
    def carId(self):
        return self.__carId

    @property
    def userId(self):
        return self.__userId

    @property
    def carCategory(self):
        return self.__carCategory
    @property
    def pickUpDate(self):
        return self.__pickUpDate
    
    @property
    def returnDate(self):
        return self.__returnDate
    
    @property
    def status(self):
        return self.__status

    @property
    def deleted(self):
        return self.__deleted
#Setters
    @carId.setter
    def carId(self, value):
        self.__carId = value

    @userId.setter
    def userId(self, value):
        self.__userId = value

    @carCategory.setter
    def carCategory(self, value):
        self.__carCategory = value

    @pickUpDate.setter
    def pickUpData(self, value):
        self.__pickUpDate = value

    @returnDate.setter
    def returnDate(self, value):
        self.__returnDate = value
    @status.setter
    def status(self, value):
        self.__status = value

    @deleted.setter
    def deleted(self, value):
        self.__deleted = value
