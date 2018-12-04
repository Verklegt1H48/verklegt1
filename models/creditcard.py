class CreditCard:
   
    def __init__(self):
        self._nameOnCard = ""
        self._number = ""
        self._cvv = ""
        self._expMonth = ""
        self._expYear = ""

    @property
    def nameOnCard(self):
        return self._nameOnCard

    @property
    def number(self):
        return None

    @property
    def cvv(self):
        return None

    @property
    def expMonth(self):
        return None

    @property
    def expYear(self):
        return None
    @nameOnCard.setter
    def nameOnCard(self, value):
        self._nameOnCard = value
    
    @number.setter
    def number(self, value):
        self._number = value

    @cvv.setter
    def cvv(self, value):
        self._cvv = value

    @expMonth.setter
    def expMonth(self, value):
        self._expMonth = value

    @expYear.setter
    def expYear(self, value):
        self._expYear = value

    def __repr__(self):
        return print("XXXX-XXXX-XXXX" + self._number[12:15] + "\n" + self._expMonth + "/" + self._expYear)

    

    def deleteCard(self):
        del self._nameOnCard
        del self._number
        del self._cvv
        del self._expMonth
        del self._expYear