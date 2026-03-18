import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

print(Fore.CYAN + "Welcome to Sentiment Spy")

user_name = input(Fore.MAGENTA + "Enter your name :- " + Style.RESET_ALL).strip()

if user_name == "":
    user_name = "Mystery Agent"

conversation_history = []

print(Fore.CYAN + f"Hello Agent {user_name}")
print("Type a sentence and I will analyze your mood")
print("Type", Fore.YELLOW + "reset", Fore.CYAN + ",", Fore.YELLOW + "history", Fore.CYAN + ",", Fore.YELLOW + "exit")

while True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()

    if not user_input:
        print(Fore.RED + "ENTER VALID TEXT")
        continue

    elif user_input.lower() == "exit":
        print(f"Exiting Sentiment Agent, Bye agent {user_name}!!!")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(Fore.CYAN + "ALL CONVERSATION REMOVED")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print("No history yet")
        else:
            print("Conversation history :- ")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😄"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "☹️"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(f"{idx}. {color}{emoji} {text}")
                print(f"   Polarity: {polarity:.2f}")
        continue

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😄"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "☹️"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))

    print(f"{color}{emoji} {sentiment_type} sentiment detected!")
    print(f"Polarity: {polarity:.2f}")
