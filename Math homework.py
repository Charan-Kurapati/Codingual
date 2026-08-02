import math

angle = float(input("Enter angle in degrees here:"))

# convert degrees into radians
radians = math.radians(angle)

# calculate trigonometric values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# display results
print("sin(", angle, ") = ", sin_value)
print("cos(", angle, ") = ", cos_value)
print("tan(", angle, ") = ", tan_value)