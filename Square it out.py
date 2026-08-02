def square(start_value,end_value):
    squares = []
    for i in range(start_value,end_value+1):
        squares.append(i*i)

    # separate odd and even values
    odd_squares = []
    even_squares = []
    for v in squares:
        if v % 2 == 0:
            even_squares.append(v)
        else:
            odd_squares.append(v)
    print("Squares values:",squares)
    print("Odd square values:",odd_squares)
    print("Even square values:",even_squares)

# enter input values
start_value = int(input("Enter start value:"))
end_value = int(input("Enter end value:"))

square(start_value,end_value)
