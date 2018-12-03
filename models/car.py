class Car:
    def __init__(self,car,catagory,manufacturer,model,year,milage,seats,transmission,extras):
        self.id = len(getCarList()) + 1
        self.deleted = 0
        #self.rentHistory = [][]
