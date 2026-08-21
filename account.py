
class Account:

    def __init__(self,owner,pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self):
        print("Account Owner",self.owner)
        print("PIN is safely stored inside class")

    def check_pin(self,pin):
        if pin == self.__pin:
            print("Access granted")
        else:
            print("Access denied")

    def set_pin(self,new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully")
        else:
            print("--ERROR--: PIN must be 4 digits!")

    def __str__(self):
        return "Account owner: "+self.owner

my_account = Account("Charan","6721")
print(my_account)
print("Checking PIN",my_account.check_pin("6721"))
my_account.__pin = "9999"
print("Checking PIN:9999:",my_account.check_pin("9999"))
print("Checking PIN:6721:",my_account.check_pin("6721"))
my_account.set_pin("9999")