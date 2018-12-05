from repositories.orderrepository import OrderRepository

class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()

    def addOrder(self, order):
        #if self.isValidCar(car):
        self.__order_repo.addOrder(order)
    
    
    def getOrderList(self):
        return self.__order_repo.getOrderList()
 
   # def get_car_category(car, category):
        
