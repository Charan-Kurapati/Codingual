from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk and run.")

class snake(animal):
    def move(self):
        print("I can crawl.")

class dog(animal):
    def move(self):
        print("I can bark.")

class lion(animal):
    def move(self):
        print("I can roar.")

obj1=human()
obj1.move()
obj2=snake()
obj2.move()
obj3=dog()
obj3.move()
obj4=lion()
obj4.move()