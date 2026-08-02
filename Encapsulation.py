class myclass:
    __privatevar=27
    def __privmeth(self):
        print("I am inside my class:myclass")
    def hello(self):
        print("private variable value",myclass.__privatevar)

obj1=myclass()
obj1.hello()

#computer class

class computer:
    def __init__(self):
        self.__max_price=900
    def sell(self):
        print("Selling price is:",self.__max_price)
    def set_max_price(self,price):
        self.__max_price=price

c=computer()
c.sell()

# change the price

c.__max_price = 1000

c.sell()

# using setter function

c.set_Max_Price(1000)

c.sell()