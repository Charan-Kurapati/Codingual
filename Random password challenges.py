import random
import string

length = int(input("Enter password length:"))

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

password = []

for i in range(length):
    password.append(random.choice(characters))

random.shuffle(password)
password = "".join(password)
print("Your password is:", password)