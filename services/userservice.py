from repositories.userrepository import UserRepository
from models.user import User
import getpass
class UserService:

    def __init__(self):
        self.__userRepo = UserRepository()
        self.__users = self.__userRepo.getUserList()

    def addUser(self, newUser):
        newUser.id = len(self.__users)
        self.__users.append(newUser)
        self.__userRepo.addUser(newUser)

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
