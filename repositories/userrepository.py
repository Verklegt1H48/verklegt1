from models.user import User
import csv
import os


class UserRepository:

    def __init__(self):
        self._userList = []
        self.__fieldnames = ["ID","Name","SocialNumber","DriversLicense",
                             "Address","Phone","Email","Password","NameOnCard","Number","CVV","ExpMonth","ExpYear"]

    # Function to write user objects into a file
    def userDictWriter(self, user, file):
        writer = csv.DictWriter(file, self.__fieldnames, restval = "", delimiter=",")
        writer.writerow({'ID'             : user.id,
                         'Name'           : user.name,
                         'SocialNumber'   : user.socialNumber,
                         'DriversLicense' : user.driverLicense,
                         'Address'        : user.address,
                         'Phone'          : user.phone,
                         'Email'          : user.email,
                         'Password'       : user.password,
                         'NameOnCard'     : user.nameOnCard,
                         'Number'         : user.number,
                         'CVV'            : user.cvv,
                         'ExpMonth'       : user.expMonth,
                         'ExpYear'        : user.expYear})
                       
                        

    # Function to open users.csv and add an instance of user to the end of the file
    def addUser(self, user):
        isEmpty = not os.path.isfile('./data/users.csv')
        with open("./data/users.csv", "a+", newline = '') as userData:
            if isEmpty:
                csv.writer(userData).writerow(self.__fieldnames)
            self.userDictWriter(user, userData)

    # Function to open users.csv and overwrite the whole list with an updated list of users.
    def overwriteusers(self, users):
        with open("./data/users.csv", "w+", newline = '') as userData:
            csv.writer(userData).writerow(self.__fieldnames)
            for user in users:
                self.userDictWriter(user, userData)

    def getUserList(self):
        if self._userList == []:
            try:
                with open("./data/users.csv", "r") as userData:
                    userDict = csv.DictReader(userData)
                    for user in userDict:
                        newUser = User()
                        newUser.id              = user['ID']
                        newUser.name            = user['Name']
                        newUser.socialNumber    = user['SocialNumber']
                        newUser.driverLicense   = user['DriversLicense']
                        newUser.address         = user['Address']
                        newUser.phone           = user['Phone']
                        newUser.email           = user['Email']
                        newUser.password        = user['Password']
                        newUser.nameOnCard      = user['NameOnCard']
                        newUser.number          = user['Number']
                        newUser.cvv             = user['CVV']
                        newUser.expMonth        = user['ExpMonth']
                        newUser.expYear         = user['ExpYear']
                        self._userList.append(newUser)
            except FileNotFoundError:
                pass
        return self._userList

