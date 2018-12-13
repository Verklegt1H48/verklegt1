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
            print("Invalid name length")
            return True
        else:
            return False

    def isValidEmail(self, email):
        if email == "q":
            sys.exit()
        elif "@" not in email:
            print("Invalid email address! Please enter a valid email address")
            return True
        else:
            return False

    def isValidPassword(self, password):
        if password == "q":
            sys.exit()
        elif len(password) < 8:
            print("Passwords must be at least 8 characters long")
            return True
        elif len(password) > 30:
            print("Password is too long")
            return True
        else:
            return False

    def isValidSocialNumber(self, socialNumber):
        if socialNumber == "q":
            sys.exit()
        elif socialNumber.isdecimal() == False:
            print("Social security number can only contain numbers")
            return True
        elif len(socialNumber) != 10:
            print("Social security number must be 10 digits long")
            return True
        else:
            return False

    def isValidDriverLicense(self, driverLicense):
        if driverLicense == "q":
            sys.exit()
        elif driverLicense.isdecimal() == False:
            print("Driver license ID can only contain numbers")
            return True
        elif len(driverLicense) != 9:
            print("Driver license ID must be 9 digits long")
            return True
        else:
            return False

    def isValidAddress(self, address):
        if address == "q":
            sys.exit()
        elif len(address) <= 0:
            print("Invalid address!")
            return True
        else:
            return False

    def isValidPhone(self, phone):
        if phone == "q":
            sys.exit()
        elif phone.isdecimal() == False:
            print("Phone number can only contain numbers")
            return True
        elif len(phone) < 7:
            print("Phone number must be at least 7 digits long")
            return True
        else:
            return False

    def isValidNameOnCard(self, nameOnCard):
        if nameOnCard == "q":
            sys.exit()
        elif len(nameOnCard) > 50 or len(nameOnCard) <= 0:
            print("Invalid name length")
            return True
        else:
            return False

    def isValidNumber(self, number):
        if number == "q":
            sys.exit()
        elif number.isdecimal() == False:
            print("Credit card number can only contain numbers")
            return True
        elif len(number) != 16:
            print("Credit card number must be 16 digits long")
            return True
        else:
            return False

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
        elif int(expYear) < year :
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

#Setterar
    @users.setter
    def users(self, value):
        self.__users = value