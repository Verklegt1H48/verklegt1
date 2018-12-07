from models.history import History
import csv

class HistoryRepository:

    def __init__(self):
        self.__history = []
        self.__fieldnames = ["Car Id", "User Id", "Order Id", "Rent History"]
    
    def historyDictWriter(self, history, file):
        Writer = csv.DictWriter(file, self.__fieldnames, restval= "", delimiter=",")
        Writer.writerow({'Car I' : history.carId,
                         'User Id': history.userId,
                         'Order Id': history.orderId,
                         'Rent History' : str(history.rentHistory).strip("[']").replace("', '",",")})
    
    def addHistory(self, history):
        with open("./data/history.csv", "a+", newline = '') as historyData:
            self.historyDictWriter(history, historyData)
    
    def getHistoryList(self):
        self.__history = []
        with open("./data/history.csv", "r") as historyData:
            historyDict = csv.DictReader(historyData)
            for history in historyDict:
                newHistory = History()
                newHistory.carId = history["Car Id"]
                newHistory.userId = history["User Id"]
                newHistory.orderId = history["Order Id"]
                newHistory.rentHistory = history["Rent History"].strip("").split(",")
                
                self.__history.append(newHistory)
        return self.__history