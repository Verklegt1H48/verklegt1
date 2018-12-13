class Order:

    def __init__(self, userId = 0, carCategory = "", carId = -1, payMethod = "", pickUpDate = "", 
                 returnDate = "", status = 0, deleted = 0):
        self.__id = 0
        self.__userId = userId
        self.__carCategory = carCategory
        self.__carId = carId
        self.__payMethod = payMethod
        self.__status = status
        self.__deleted = deleted
        self.__pickUpDate = pickUpDate
        self.__returnDate = returnDate

    def __repr__(self):
        return "{:7}{:8}{:10}{:7}{:16}{:15}{:10}".format("", str(self.__userId), self.__carCategory,
                                                         str(self.__carId), self.__payMethod,
                                                         self.__pickUpDate, self.__returnDate)


#Getters
    @property
    def id(self):
        return self.__id

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
    def payMethod(self):
        return self.__payMethod

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
    @id.setter
    def id(self, value):
        self.__id = int(value)

    @carId.setter
    def carId(self, value):
        self.__carId = int(value)

    @userId.setter
    def userId(self, value):
        self.__userId = int(value)

    @carCategory.setter
    def carCategory(self, value):
        self.__carCategory = value

    @payMethod.setter
    def payMethod(self, value):
        self.__payMethod = value
    
    @pickUpDate.setter
    def pickUpDate(self, value):
        self.__pickUpDate = value

    @returnDate.setter
    def returnDate(self, value):
        self.__returnDate = value
    
    @status.setter
    def status(self, value):
        self.__status = int(value)

    @deleted.setter
    def deleted(self, value):
        self.__deleted = int(value)
