import colorama
from colorama import Fore
from textblob import TextBlob

colorama.init(autoreset=True)

print(Fore.CYAN + "Welcome to Sentiment Spy")

user_name = input(Fore.MAGENTA + "Enter your name :- ").strip()

if user_name == "":
    user_name = "Mystery Agent"

history = []

print(Fore.CYAN + f"Hello Agent {user_name}")
print("Type something to analyze mood")
print("Commands: reset, history, stats, undo, exit")

while True:
    user_input = input(Fore.GREEN + ">> ").strip()

    if not user_input:
        print(Fore.RED + "Enter valid text")
        continue

    cmd = user_input.lower()

    if cmd == "exit":
        print("Goodbye Agent", user_name)
        break

    elif cmd == "reset":
        history.clear()
        print("History cleared")
        continue

    elif cmd == "history":
        if not history:
            print("No history yet")
        else:
            for i, (text, pol, sent) in enumerate(history, 1):
                print(f"{i}. {text} ({sent}, {pol:.2f})")
        continue

    elif cmd == "stats":
        if not history:
            print("No data")
        else:
            avg = sum(x[1] for x in history) / len(history)
            print(f"Average mood: {avg:.2f}")
        continue

    elif cmd == "undo":
        if history:
            removed = history.pop()
            print(Fore.YELLOW + f"Removed: {removed[0]}")
        else:
            print("Nothing to undo")
        continue

    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😄"
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "☹️"
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    history.append((user_input, polarity, sentiment))

    print(f"{color}{emoji} {sentiment}")
    print(f"Polarity: {polarity:.2f}")
