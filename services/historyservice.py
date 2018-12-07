from repositories.historyrepository import HistoryRepository
from operator import attrgetter, methodcaller
from models.history import History

class HistoryService:
    def __init__(self):
        self.__historyRepo = HistoryRepository()
    
   # def addHistory(self):
    #    newHistory = History()
     #   newHistory.
     
    def getHistoryList(self):
        return self.__historyRepo.getHistoryList()
    