empty_list=[]
print(empty_list)

list_1=[38,86,21,97,43]
print(list_1)

triples=[1,2,3,4,5]*3
print(triples)

list_2=[100,200,300,400,500]
list_2=list_2[::-1]
print(list_2)


#Word matching

def match_words(words):
    ctr=0
    list=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            list.append(word)
    print("List of words with first and last character same\n", list)
    return ctr

count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])

print("Number of words having first and last character same:", count)