num1=[1,2,3,4,5]

num2=[1,3,5,9,6]

result = map(lambda x, y: x + y, num1, num2)

print("The 2 lists added are:",list(result))

def sq(n):

    return n*n

square = list(map(sq, num2))

print(square)