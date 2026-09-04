print("Hello Iam AI bot what is your name?")
name = input()
print("Nice to meet you",name,"!")
print("How are you feeling today?(good/bad)")
mood = input().lower()

if mood == "good":
    print("I am glad to hear that!")

elif mood == "bad":
    print("I am sorry to hear that.Hope things get better soon...")

else:
    print("I see,sometimes it is hard to put feelings into words...")

print("It was nice chatting with you",name,"Goodbye!")