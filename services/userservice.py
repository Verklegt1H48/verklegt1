from repositories.userrepository import UserRepository
from models.user import User
from datetime import datetime
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

    def getUserBySocial(self, socialNumber):
        for user in self.__users:
            if user.socialNumber == socialNumber:
                return user
        return "Not found"

    def deleteUser(self, user):
        user.deleteUser()

    def isDeleted(self, user):
        #Todo: Implement
        return user.deleted()

    def isValidName(self, name):
        if name == "q":
            exit(1)
        elif len(name) > 50 or len(name) <= 0:
            print("Invalid name length")
            return True
        else:
            return False

    def isValidEmail(self, email):
        if email == "q":
            exit(1)
        elif "@" not in email:
            print("Invalid email address! Please enter a valid email address")
            return True
        else:
            return False

    def isValidPassword(self, password):
        if password == "q":
            exit(1)
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
            exit(1)
        elif len(socialNumber) != 10:
            print("Social security number must be 10 digits long")
            return True
        else:
            return False

    def isValidDriverLicense(self, driverLicense):
        if driverLicense == "q":
            exit(1)
        elif len(driverLicense) != 9:
            print("Driver license ID must be 9 digits long")
            return True
        else:
            return False

    def isValidAddress(self, address):
        if address == "q":
            exit(1)
        elif len(address) <= 0:
            print("Invalid address!")
            return True
        else:
            return False

    def isValidPhone(self, phone):
        if phone == "q":
            exit(1)
        elif len(phone) < 7:
            print("Phone number must be at least 7 digits long")
            return True
        else:
            return False

    def isValidNameOnCard(self, nameOnCard):
        if nameOnCard == "q":
            exit(1)
        elif len(nameOnCard) > 50:
            print("Name is too long")
            return True
        else:
            return False

    def isValidNumber(self, number):
        if number == "q":
            exit(1)
        elif len(number) > 23:#!= 16:
            print("Credit card number must be 16 digits long")
            return True
        else:
            return False

    def isValidCvv(self, cvv):
        if cvv == "q":
            exit(1)
        elif len(cvv) != 3:
            print("CVV code must be 3 digits long")
            return True
        else:
            return False

    def isValidExpMonth(self, expMonth):
        if expMonth == "q":
            exit(1)
        elif len(expMonth) > 2:
            print("Invalid input!")
            return True
        elif int(expMonth) <= 0 or int(expMonth) > 12:
            print("Month does not exist")
            return True
        else:
            return False

    def isValidExpYear(self, expYear, expMonth):
        year = int(datetime.today().year) - 2000
        #month = int(datetime.today().month)
        if expYear == "q":
            exit(1)
        elif int(expYear) < year :
            print("Card is Expired")
            return False
        #elif int(expYear) == year:
         #   if int(expMonth) <= month:
          #      print("Card is expired")
           #     return False
        else:
            return True

    def getUserList(self):
        return self.__users