from models.user import User
import csv

class UserRepository:

    def __init__(self):
        self._userList = []
        self.__fieldnames = ["ID","Name","SocialNumber","DriversLicense","Address","Phone","Email","Pin"]



    def addUser(self, user):
        with open("./data/users.csv", "a+") as usersFile:
            name = user.name()
            id = user.id()
            socialNumber = user.socialNumber()
            driverLicense = user.driverLicense()
            address = user.address()
            phone = user.phone()
            email = user.email()
            pin = user.pin()
            usersFile.write("{},{},{},{},{},{},{},{},\n".format(name, id,\
            socialNumber, driverLicense, address, phone, email, pin))
            
    def getUserList(self):
        if self._userList == []:
            with open("./data/users.csv", "r") as userData:
                userDict = csv.DictReader(userData)
                for user in userDict:
                    newUser = User()
                    newUser.id              = user['id']
                    newUser.name            = user['name']
                    newUser.socialNumber    = user['socialNumber']
                    newUser.driverLicense   = user['driverLicense']
                    newUser.address         = user['address']
                    newUser.phone           = user['phone']
                    newUser.email           = user['email']
                    self._userList.append(newUser)
        return self._userList

    def getUser(self, id):
        with open("./data/users.csv", "r") as userData:
            userDict = csv.DictReader(userData)
            for user in userDict:
                if id == user['id']:
                    newUser = User()
                    newUser.id              = user['id']
                    newUser.name            = user['name']
                    newUser.socialNumber    = user['socialNumber']
                    newUser.driverLicense   = user['driverLicense']
                    newUser.address         = user['address']
                    newUser.phone           = user['phone']
                    newUser.email           = user['email']
                    return newUser
        return 0 #Returnar 0 til að byrja með
         

