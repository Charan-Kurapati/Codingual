class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    pass
school_bus=bus("Electric Volvo",160,10)

print("School bus name",school_bus.name,"School bus max",school_bus.max_speed,"School bus mileage",school_bus.mileage)


#person

class person:
    def __init__(self,name,IDnumber):
        self.name=name
        self.IDnumber=IDnumber
    def display(self):
        print(self.name)
        print(self.IDnumber)

class employee(person):
    def __init__(self,name,IDnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,IDnumber)

obj1=employee("Jake",2067,1000,"manager")

obj1.display()