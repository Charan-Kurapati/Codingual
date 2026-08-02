import math

dc=int(input("Enter degree celsius:"))

if dc < 20:
    print("You need to wear both jacket and pullover.")
elif dc >=20 and dc <=27:
    print("You can wear a jacket or pullover.")
elif dc > 28:
    print("You do not need to wear a jacket or pullover.")