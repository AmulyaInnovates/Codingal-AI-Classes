import re
import random
from colorama import Fore, init

init(autoreset=True)

# Data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

weather_data = {
    "bali": "Sunny and tropical",
    "maldives": "Hot and sunny",
    "phuket": "Humid weather",
    "tokyo": "Mild weather",
    "paris": "Cool and slightly rainy",
    "new york": "Variable weather"
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers feel warm? Because of hot spots!"
]

favorites = []
history = []

# Helper
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Recommendation (loop-based)
def recommend(name):
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    
    while True:
        preference = normalize_input(input(Fore.YELLOW + "You: "))

        if preference in destinations:
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: {name}, how about {suggestion}?")
            
            history.append(suggestion)

            print(Fore.CYAN + "Do you like it? (yes/no)")
            answer = normalize_input(input("You: "))

            if answer == "yes":
                print(Fore.GREEN + f"Great! Enjoy your trip to {suggestion}!")
                
                save = normalize_input(input("Save to favorites? (yes/no): "))
                if save == "yes":
                    favorites.append(suggestion)
                    print(Fore.MAGENTA + "Added to favorites!")
                break
            elif answer == "no":
                print(Fore.RED + "Okay, trying another...")
            else:
                print(Fore.RED + "Please answer with yes or no.")
        else:
            print(Fore.RED + "Invalid choice. Try again.")

# Packing tips
def packing_tips():
    location = normalize_input(input("Where to? "))
    days = input("How many days? ")

    if not days.isdigit():
        print(Fore.RED + "Enter a valid number of days.")
        return

    days = int(days)

    print(Fore.GREEN + f"\nPacking tips for {days} days in {location}:")
    print("- Clothes:", days // 2 + 1, "sets")
    print("- Chargers / Power bank")
    print("- Basic medicines")
    print("- Check weather before leaving")

# Weather
def weather():
    place = normalize_input(input("Enter destination: "))
    print(Fore.GREEN + "Weather:", weather_data.get(place, "No data available"))

# Favorites
def show_favorites():
    if not favorites:
        print(Fore.RED + "No favorites yet.")
    else:
        print(Fore.MAGENTA + "Your favorite places:")
        for f in favorites:
            print("-", f)

# History
def show_history():
    if not history:
        print(Fore.RED + "No history yet.")
    else:
        print(Fore.CYAN + "Your previous suggestions:")
        for h in history:
            print("-", h)

# Joke
def tell_joke():
    print(Fore.YELLOW + random.choice(jokes))

# Help
def show_help():
    print(Fore.MAGENTA + """
Commands:
recommend  → get travel suggestions
packing    → packing tips
weather    → check weather
favorites  → show saved places
history    → show past suggestions
joke       → hear a joke
help       → show menu
exit       → quit
""")

# Main chat
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input("Your name: ")

    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = normalize_input(input(Fore.YELLOW + f"{name}: "))

        if user_input == "recommend":
            recommend(name)
        elif user_input == "packing":
            packing_tips()
        elif user_input == "weather":
            weather()
        elif user_input == "favorites":
            show_favorites()
        elif user_input == "history":
            show_history()
        elif user_input == "joke":
            tell_joke()
        elif user_input == "help":
            show_help()
        elif user_input in ["exit", "bye"]:
            print(Fore.CYAN + "TravelBot: Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: I did not understand that.")

if __name__ == "__main__":
    chat()
