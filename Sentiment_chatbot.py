import time
from datetime import datetime
from textblob import TextBlob
from colorama import init, Fore, Style

init(autoreset=True)

conversation_history = []
sentiment_counts = {
    "positive": 0,
    "negative": 0,
    "neutral": 0
}


def show_processing_animation():
    """Show a simple spy-themed loading animation."""
    messages = [
        "Agent Bot is scanning your message",
        "Analysing emotional clues",
        "Preparing sentiment report"
    ]

    for message in messages:
        print(Fore.CYAN + message, end="")
        for _ in range(3):
            time.sleep(0.25)
            print(".", end="", flush=True)
        print()


def analyze_sentiment(text):
    """Classify text as positive, negative, or neutral."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, polarity


def display_sentiment(text, sentiment, polarity):
    """Show the result using a colour and a friendly message."""
    if sentiment == "positive":
        colour = Fore.GREEN
        message = "Great! Your message sounds positive."
    elif sentiment == "negative":
        colour = Fore.RED
        message = "Your message sounds negative."
    else:
        colour = Fore.YELLOW
        message = "Your message sounds neutral."

    strength = abs(polarity)

    print(colour + "\n--- SENTIMENT RESULT ---")
    print(f"Message: {text}")
    print(f"Sentiment: {sentiment.upper()}")
    print(f"Polarity score: {polarity:.2f}")
    print(f"Sentiment strength: {strength:.2f} (0 = weak, 1 = strong)")
    print(message)
    print(Style.RESET_ALL)


def execute_command(command):
    """Run commands such as summary, reset, history, and help."""
    command = command.lower().strip()

    if command == "summary":
        print_summary()
        return True

    elif command == "reset":
        conversation_history.clear()
        for sentiment in sentiment_counts:
            sentiment_counts[sentiment] = 0
        print(Fore.CYAN + "All stored conversation and sentiment data has been reset.")
        return True

    elif command == "history":
        if not conversation_history:
            print("No messages have been analysed yet.")
        else:
            print(Fore.CYAN + "\n--- CONVERSATION HISTORY ---")
            for number, item in enumerate(conversation_history, start=1):
                print(
                    f"{number}. {item['text']} | "
                    f"{item['sentiment'].upper()} | "
                    f"Polarity: {item['polarity']:.2f}"
                )
        return True

    elif command == "help":
        print_help()
        return True

    return False


def print_summary():
    """Display the current sentiment totals."""
    total = sum(sentiment_counts.values())

    print(Fore.CYAN + "\n--- SENTIMENT SUMMARY ---")
    print(f"Total messages analysed: {total}")
    print(f"Positive messages: {sentiment_counts['positive']}")
    print(f"Negative messages: {sentiment_counts['negative']}")
    print(f"Neutral messages:  {sentiment_counts['neutral']}")


def print_help():
    """List all available commands."""
    print(Fore.CYAN + "\n--- AVAILABLE COMMANDS ---")
    print("Type any sentence to analyse its sentiment.")
    print("summary - Show the sentiment totals")
    print("reset   - Clear the history and all sentiment counts")
    print("history - Show previously analysed messages")
    print("help    - Show this list of commands")
    print("exit    - End the chatbot and save a report")


def get_valid_name():
    """Ask for a name containing only alphabetic characters."""
    while True:
        name = input("Agent, please enter your first name: ").strip()

        if name.isalpha():
            return name
        else:
            print(Fore.RED + "Please use letters only, with no spaces or numbers.")


def save_final_report(username):
    """Print and save the final sentiment report."""
    total = sum(sentiment_counts.values())
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = [
        "SENTIMENT ANALYSIS CHATBOT - FINAL REPORT",
        "=" * 42,
        f"Username: {username}",
        f"Date and time: {now}",
        "",
        f"Total messages analysed: {total}",
        f"Positive messages: {sentiment_counts['positive']}",
        f"Negative messages: {sentiment_counts['negative']}",
        f"Neutral messages: {sentiment_counts['neutral']}",
        "",
        "MESSAGE HISTORY",
        "-" * 42
    ]

    if conversation_history:
        for number, item in enumerate(conversation_history, start=1):
            report.append(f"{number}. Message: {item['text']}")
            report.append(f"   Sentiment: {item['sentiment'].upper()}")
            report.append(f"   Polarity: {item['polarity']:.2f}")
    else:
        report.append("No messages were analysed.")

    filename = f"{username}_sentiment_analysis.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(report))

        print(Fore.GREEN + "\n--- FINAL REPORT ---")
        print("\n".join(report))
        print(Fore.GREEN + f"\nReport saved successfully as: {filename}")

    except OSError as error:
        print(Fore.RED + f"Could not save the report: {error}")


def main():
    """Run the chatbot."""
    print(Fore.CYAN + "=" * 45)
    print(Fore.CYAN + "   WELCOME TO AGENT BOT: SENTIMENT SPY")
    print(Fore.CYAN + "=" * 45)
    print("I can analyse whether a message sounds positive, negative, or neutral.\n")

    username = get_valid_name()
    print(Fore.GREEN + f"\nWelcome, Agent {username}!")
    print("Type a sentence to analyse it, or type 'help' for commands.")
    print("Type 'exit' whenever you want to finish.\n")

    while True:
        user_input = input(Fore.WHITE + "You: ").strip()

        if not user_input:
            print(Fore.YELLOW + "Please enter a sentence or a command.")
            continue

        if user_input.lower() == "exit":
            print(Fore.CYAN + "\nAgent, your mission is complete.")
            save_final_report(username)
            break

        if user_input.lower() in ["summary", "reset", "history", "help"]:
            execute_command(user_input)
            continue

        show_processing_animation()
        sentiment, polarity = analyze_sentiment(user_input)

        sentiment_counts[sentiment] += 1
        conversation_history.append({
            "text": user_input,
            "sentiment": sentiment,
            "polarity": polarity
        })

        display_sentiment(user_input, sentiment, polarity)


if __name__ == "__main__":
    main()