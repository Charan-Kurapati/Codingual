class Vehicle:
    def __init__(self,brand,max_speed,):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Brand:",self.brand)
        print("Max speed:",self.max_speed,"km/h")

class Car(Vehicle):
    def __init__(self,brand,max_speed,model,seats):
        self.model = model
        self.seats = seats
        super().__init__(brand,max_speed)

    def show_details(self):
        print("Car Model:",self.model)
        print("Number of seats:",self.seats)

        super().show_details()

    def fuel_type(self):
        print("Fuel Type:Petrol")

my_car = Car("Volvo",180,"XC60",5)

print("----Car Details----")
my_car.show_details()

print()

my_car.fuel_type()

print()

print("Is car a subclass of Vehicle?")
print(issubclass(Car,Vehicle))