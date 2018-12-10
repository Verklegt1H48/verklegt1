from repositories.userrepository import UserRepository
from models.user import User
import getpass
class UserService:

    def __init__(self):
        self.__userRepo = UserRepository()
        self.__users = self.__userRepo.getUserList()

    #def getUser(self):
    #   return self.__userRepo.getUser(id)

    def addUser(self, newUser):
        self.__users.append(newUser)
        self.__userRepo.addUser(newUser)

#    def getUserBySocial(self, social):
#        for i in self.__users:
#            if self.__userRepo.__userList[i].social == social:
#                return self.__userRepo.__userList[i]
#        
#        raise ValueError("User not found")
#    
#    def getUserById(self, id):
#        for i in self.__userRepo.__userList:
#            if self.__userRepo.__userList[i].id == id:
#                return self.__userRepo.__userList[i]
#        
#        raise ValueError("User not found")
#
#    def getUserByLicense(self, license):
#        for i in self.__userRepo.__userList:
#            if self.__userRepo.__userList[i].driverLicense == license:
#                return self.__userRepo.__userList[i]
#        raise ValueError("User not found")
     #   return self._userRepo.getUser(id)

    def getUserByEmail(self, email):
        for user in self.__users:
            if user.email == email:
                return user
        return "Not found"

    def isEmployee(self, user):
        return user.employee()

    def updateUser(self, user):
        #Todo: Implement
        return 

    def deleteUser(self, user):
        user.deleteUser()

    def isDeleted(self, user):
        #Todo: Implement
        return user.deleted()
