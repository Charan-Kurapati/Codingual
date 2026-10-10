def Chatbot():
    print("Welcome to the Enhanced Chatbot!")
    name = input("What is your name?:")
    print(f"Hello,{name}! Nice to meet you.")
    print("I am here to have a frindly chat with you.")

    while True:
        mood = input(
            "\nHow are you feeling today? (good,bad or neutral):"
        ).lower()

        if mood =="good":
            print("That's wonderful! Keep smiling!")
        elif mood == "bad":
            print("I'm sorry to hear that. I hope things get better!")
        elif mood == "neutral":
            print("That's okay! Every day can be different.")
        else:
            print("I don't recognise that mood, but thanks for sharing!")

        hobby = input(
            "What is your favourite hobby or activity?"
        )
        print(f"That sounds interesting,{name}!")
        print(f"I hope you enjoy {hobby}.")

        choice = input(
            "\nwould you like to continue chatting? (Yes/No):"
        ).lower()

        if choice == "no":
            print(f"\nIt was lovely chatting with you,{name}!")
            print("Goodbye! Have a fantastic day!")
            break

        elif choice == "yes":
            print(f"\nGreat,{name}! Let's chat again")

        else:
            print("I didn't understand.Let's continue chatting")

Chatbot()