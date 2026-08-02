class Dog:
    animal="Dog"
    def __init__(self,breed,colour):
        self.breed = breed
        self.colour = colour

    def display_details(self):
        print("Animal:",Dog.animal)
        print("Breed:",self.breed)
        print("Colour:",self.colour)
        print("-----------------------")

dog1 = Dog("German Shepard","Black and Brown")
dog2 = Dog("Pomeranian","Golden Brown")

print("Dog1 details:")
dog1.display_details()
print("Dog2 details:")
dog2.display_details()