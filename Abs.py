from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed value:" , x)
    @abstractmethod
    def task(self):
        print("We are inside abs_class")

class test_class(absclass):
    def task(self):
        print("We are inside test_class.")

obj1=test_class()
obj1.task()
obj1.print(11)