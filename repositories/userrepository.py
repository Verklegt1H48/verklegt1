from models.user import User
class UserRepository:

    def __init__(self):
        self._users = []


    def addUser(self, user):
        with open("./data/users.txt", "a+") as usersFile:
            name = user.name()
            id = user.id()
            socialNumber = user.socialNumber()
            driverLicense = user.driverLicense()
            address = user.address()
            phone = user.phone()
            email = user.email()
            usersFile.write("{},{},{},{},{},{},{}\n".format(name, id,\
            socialNumber, driverLicense, address, phone, email))
            
    def getUsers(self):
        if self._users == []:
            with open("./data/videos.txt", "r") as userFile:
                for line in userFile.readlines():
                    name, id, socialNumber, driverLicense,\
                    address, phone, email = line.split(",")
                    newUser = User(name, id, socialNumber,\
                    driverLicense, address, phone, email)
                    self._users.append(newUser)
        return self._users
         

