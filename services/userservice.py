from repositories.userrepository import UserRepository
from models.user import User
from datetime import datetime
import getpass, sys
class UserService:


    def __init__(self):
        self.__userRepo = UserRepository()
        self.__users = self.__userRepo.getUserList()

    def addUser(self, newUser):
        newUser.id = len(self.__users)
        self.__users.append(newUser)
        self.__userRepo.addUser(newUser)

    def updateUser(self, userToUpdate):
        for user in self.__users:
            if user.id == int(userToUpdate.id):
                user = userToUpdate
            self.__userRepo.overwriteUsers(self. __users)

    def getUserByEmail(self, email):
        for user in self.__users:
            if user.email == email:
                return user
        return "Not found"

    def getUserBySocial(self, socialNumber):
        for user in self.__users:
            if user.socialNumber == socialNumber:
                return user
        return "Not found"

    def getUserListBySocial(self, socialNumber):
        userList = []
        for user in self.__users:
            if user.socialNumber == socialNumber:
                userList.append(user)
        return userList

    def deleteUser(self, userID):
        success = False
        for user in self.__users:
            if str(user.id) == str(userID):
                user.deleted = "1"
                success = True
                break
        if success:
            self.__userRepo.overwriteUsers(self.__users)
        return success

    def isValidUserId(self, UserId):
        for user in self.__users:
            if user.id == UserId and user.employee != 1 and user.deleted != 1:
                return True
        return False

    def isValidName(self, name):
        if name == "q":
            sys.exit()
        elif len(name) > 50 or len(name) <= 0:
            return "length"
        else:
            return ""

    def isValidEmail(self, email):
        if email == "q":
            sys.exit()
        elif "@" not in email:
            return "invalid"
        else:
            return ""

    def isValidPassword(self, password):
        if password == "q":
            sys.exit()
        elif len(password) < 8:
            return "short"
        elif len(password) > 30:
            return "long"
        else:
            return ""

    def isValidSocialNumber(self, socialNumber):
        if socialNumber == "q":
            sys.exit()
        elif socialNumber.isdecimal() == False:
            return "numbers"
        elif len(socialNumber) != 10:
            return "length"
        else:
            return ""

    def isValidDriverLicense(self, driverLicense):
        if driverLicense == "q":
            sys.exit()
        elif driverLicense.isdecimal() == False:
            return "numbers"
        elif len(driverLicense) != 9:
            return "length"
        else:
            return ""

    def isValidAddress(self, address):
        if address == "q":
            sys.exit()
        elif len(address) <= 0:
            return "invalid"
        else:
            return ""

    def isValidPhone(self, phone):
        if phone == "q":
            sys.exit()
        elif phone.isdecimal() == False:
            return "numbers"
        elif len(phone) < 7:
            return "length"
        else:
            return ""

    def isValidNameOnCard(self, nameOnCard):
        if nameOnCard == "q":
            sys.exit()
        elif len(nameOnCard) > 50 or len(nameOnCard) <= 0:
            return "length"
        else:
            return ""

    def isValidNumber(self, number):
        if number == "q":
            sys.exit()
        elif number.isdecimal() == False:
            return "numbers"
        elif len(number) != 16:
            return "length"
        else:
            return ""

    def isValidCvv(self, cvv):
        if cvv == "q":
            sys.exit()
        elif cvv.isdecimal() == False:
            return "numbers"
        elif len(cvv) != 3:
            return "length"
        else:
            return True

    def isValidPin(self, pin):
        if pin == "q":
            sys.exit()
        elif pin.isdecimal() == False:
            return "numbers"
        elif len(pin) != 5:
            return "length"
        else:
            return True

    def isValidExpMonth(self, expMonth):
        if expMonth == "q":
            sys.exit()
        elif not expMonth.isdecimal():
            return "NaN"
        elif len(expMonth) > 2:
            return "length"
        elif int(expMonth) <= 0 or int(expMonth) > 12:
            return "month"
        else:
            return True

    def isValidExpYear(self, expYear, expMonth):
        year = int(datetime.today().year) - 2000
        month = int(datetime.today().month)
        if expYear == "q":
            sys.exit()
        elif not expYear.isdecimal():
            return "NaN"
        elif len(expYear) > 2:
            return "length"
        elif int(expYear) < year:
            return "year"
        elif int(expYear) == year:
            if int(expMonth) <= month:
                return "year"
        else:
            return True

    def getUserList(self):
        return self.__users

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, value):
        self.__users = value
