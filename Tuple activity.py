tuple1=(19,"Hi",49,"Great",48.7)
print(tuple1)

tuple2=(40,39,92,40,28,19,82,40)
print(tuple2)

tuple2=tuple2+(9,)
print(tuple2)

print(tuple2.count(40))
slice1=tuple2[3:6]
print(slice1)

#pallindrome

def palind(r):
    e=len(r)-1
    s=0
    while (s<e):
        if (r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r=(1,2,3,3,2,1)

if(palind(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")