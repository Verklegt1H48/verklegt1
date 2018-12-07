class History:
    def __init__(self, carId = 0, userId = 0, orderId = 0):
        self.__carId = 0
        self.__userId = 0
        self.__orderId = 0
        self.__rentHistory = []
    
    #def __str__(self):
    #   return "{}, {}, {}, {}\n"
    #  .format(self.__carId, self.__userId, self.__orderId)

    @property
    def carId(self):
        return self.__carId
    
    @property
    def userId(self):
        return self.__userId
    
    @property
    def orderId(self):
        return self.__orderId
    
    @property
    def rentHistory(self):
        return self.__rentHistory

    @carId.setter
    def carId(self, carId):
        self.__carId = int(id)
    
    @userId.setter
    def userId(self, userId):
        self.__userId = int(id)

    @orderId.setter
    def orderId(self, orderId):
        self.__orderId = int(id)

    @rentHistory.setter
    def rentHistory(self, rentHistory):
        self.__rentHistory.append(rentHistory)
    


    