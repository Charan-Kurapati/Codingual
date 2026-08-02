import array as arr

array_num1=arr.array('i',[1,3,5,3,7,9,3])

print("Original array:",array_num1)

print("Number of occurances of number 3 in the array are:",array_num1.count(3))

array_num1.reverse()
print("Reverse of original array is:",array_num1)
