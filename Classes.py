class student:
    grade = 10
    print("Hi I am student of Grade",grade)

obj1 = student()


#cars

class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage= mileage

modelx = vehicle(150,15)

print("Modelx max speed is",modelx.max_speed)
print("Modelx mileage",modelx.mileage)


#parrot

class parrot:
    species = "bird" 
    def __init__(self,name,age):
        self.age = age
        self.name = name

obj1=parrot("Squawky",11)
obj2=parrot("Snowy",10)

print("Name of obj1 is:",obj1.name,)
print("Name of obj2:",obj2.name,)
print("Age of obj1:",obj1.age,)
print("Age of obj2:",obj2.age,)
print("Species of parrot is:",obj2.species)
print("{} is {} years old".format( obj1.name, obj1.age))
print("{} is {} years old".format( obj2.name, obj2.age))