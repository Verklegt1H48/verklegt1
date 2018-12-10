from repositories.userrepository import UserRepository
from models.user import User
import getpass
class UserService:

    def __init__(self):
        self._userRepo = UserRepository()
        self._users = self._userRepo.getUserList()

    #def getUser(self):
     #   return self._userRepo.getUser(id)

    def addUser(self, user):
        newUser = User()
        newUser.id              = len(self._users)
        newUser.name            = input("Full name: ")
        newUser.email           = input("Email address: ")
        newUser.password        = getpass.getpass("Password: ")
        #passConfirm = input("Confirm password: ")
        newUser.socialNumber    = input("Social security number: ")
        newUser.driverLicense   = input("Driver license ID: ")
        newUser.address         = input("Address: ")
        newUser.phone           = input("Phone number: ")
        newUser.nameOnCard      = input("Name on credit card: ")
        newUser.number          = input("Credit card number: ")
        newUser.cvv             = input("CVV: ")
        newUser.expMonth        = input("Exp month(mm): ")
        newUser.expYear         = input("Exp year(yy): ")
        self._users.append(newUser)
        self._userRepo.addUser(newUser)

    def getUserBySocial(self, social):
        for i in self._userRepo._userList:
            if self._userRepo._userList[i].social == social:
                return self._userRepo._userList[i]
        
        raise ValueError("User not found")
    
    def getUserById(self, id):
        for i in self._userRepo._userList:
            if self._userRepo._userList[i].id == id:
                return self._userRepo._userList[i]
        
        raise ValueError("User not found")

    def getUserByLicense(self, license):
        for i in self._userRepo._userList:
            if self._userRepo._userList[i].driverLicense == license:
                return self._userRepo._userList[i]
        
        raise ValueError("User not found")

    def getUserByEmail(self, email):
        for user in self._users:
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
    
