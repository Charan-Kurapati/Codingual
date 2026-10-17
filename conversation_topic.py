import random
import re
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

user_name = ""

def welcome():
    print(Fore.CYAN + "================================")
    print(Fore.YELLOW + "   MY SMART CHATBOT")
    print(Fore.CYAN + "================================")

    name = input(Fore.GREEN + "What is your name? ")
    print(Fore.MAGENTA + "Hello, " + name + "! Nice to meet you!")

    return name

def tell_joke():
    jokes = [
        "Why did the computer go to the doctor? It had a virus!",
        "Why was the maths book sad? It had too many problems!",
        "What do you call a sleeping dinosaur? A dino-snore!"
    ]

    print(Fore.YELLOW + random.choice(jokes))

def show_weather():
    print(Fore.CYAN + "Today's pretend weather is sunny and warm!")
    print("Remember: This is a simulated forecast, not live weather.")

def show_news():
    print(Fore.CYAN + "Here is some pretend news:")
    print("Scientists have invented a robot that helps water plants!")
    print("Note: This is a fictional news story.")

def show_time():
    now = datetime.now()
    print(Fore.GREEN + "The time on this computer is:",
        now.strftime("%H:%M:%S"))

def maths_game():
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)

    answer = input(
        f"What is {number1} + {number2}? "
    )

    if answer.isdigit() and int(answer) == number1 + number2:
        print(Fore.GREEN + "Correct! Well done!")
    else:
        print(Fore.RED + "Good try! The answer is",
            number1 + number2)


def chatbot_response(message, name):
    message = message.lower().strip()

    clean_message = re.sub(r"[^\w\s]", "", message)

    if any(word in clean_message.split()
        for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye " + name + "! Have a great day!"

    elif any(word in clean_message.split()
            for word in ["hello", "hi", "hey"]):
        return "Hello " + name + "! How are you today?"

    elif "your name" in clean_message:
        return "I am SmartBot, your friendly chatbot!"

    elif "weather" in clean_message:
        show_weather()
        return "Would you like to ask me something else?"

    elif "news" in clean_message:
        show_news()
        return "Would you like to hear more?"

    elif "time" in clean_message:
        show_time()
        return "Is there anything else you want to know?"

    elif any(word in clean_message.split()
            for word in ["joke", "funny", "laugh"]):
        tell_joke()
        return "I hope that made you smile!"

    elif "maths" in clean_message or "math" in clean_message:
        maths_game()
        return "Let's keep practising!"

    elif "my name" in clean_message:
        return "Your name is " + name + "!"

    elif any(word in clean_message.split()
            for word in ["thanks", "thank"]):
        return "You are welcome, " + name + "!"

    else:
        return (
            "That sounds interesting! "
            "Try asking me about weather, news, time, "
            "jokes or maths."
        )

def main():
    name = welcome()

    print(Fore.CYAN + "\nYou can ask me about:")
    print("1. Weather")
    print("2. News")
    print("3. Time")
    print("4. Jokes")
    print("5. Maths")
    print("Type 'bye' to stop chatting.\n")

    while True:
        message = input(Fore.BLUE + "You: ")

        response = chatbot_response(message, name)

        print(Fore.MAGENTA + "SmartBot: " + response)

        if re.search(
            r"\b(bye|goodbye|exit|quit)\b",
            re.sub(r"[^\w\s]", "", message.lower())
        ):
            break

if __name__ == "__main__":
    main()