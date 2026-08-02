A_set1={"blue","green"}
B_set1={1,2,3,4,5}
A_set2={"blue","yellow"}
B_set2={1,5,6,7,8,9}

result1 = A_set1.symmetric_difference(A_set2)
result2 = B_set1.symmetric_difference(B_set2)

print("First set1 is:", A_set1)
print("First set2 is:", A_set2)
print("Symmetric difference of A_set1 and A_set2 is:", result1)
print("Second set1 is:", B_set1) 
print("Second set2 is:", B_set2)
print("Symmetric difference of B_set1 and B_set2 is:", result2)