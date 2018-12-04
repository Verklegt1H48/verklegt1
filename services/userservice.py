from repositories.userrepository import UserRepository
class UserService:
    def __init__(self):
        self._userRepo = UserRepository()

    def getUsers(self):
        return self._userRepo.getUsers()

    def addUser(self, user):
        self._userRepo.addUser(user)
    

        

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
            if self._userRepo._userList[i].driverLicense == id:
                return self._userRepo._userList[i]
        
        raise ValueError("User not found")

    
    def isValidUser(self, user):
        #Todo: Implement
        return 

    def isEmployee(self, user):
        #Todo: Implement
        return 

    def updateUser(self, user):
        #Todo: Implement
        return 

    def deleteUser(self, user):
        #Todo: Implement
        return 

    def isDeleted(self, user):
        #Todo: Implement
        return 
    
