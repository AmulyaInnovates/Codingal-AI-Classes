import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found.")
    raise SystemExit

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

def senti(p):
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    data = df

    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]

    if rating is not None:
        data = data[data["IMDB_Rating"] >= rating]

    if data.empty:
        return "No suitable movie recommendations found."

    data = data.sample(frac=1).reset_index(drop=True)

    results = []
    mood_score = TextBlob(mood).sentiment.polarity if mood else 0

    for _, row in data.iterrows():
        overview = row.get("Overview")
        if pd.isna(overview):
            continue

        pol = TextBlob(overview).sentiment.polarity

        if mood and mood_score > 0 and pol < 0:
            continue

        results.append((row["Series_Title"], row["Genre"], row["IMDB_Rating"], pol))

        if len(results) == n:
            break

    return results if results else "No suitable movie recommendations found."

def random_recommend(n=5):
    sample = df.sample(n)
    results = []

    for _, row in sample.iterrows():
        pol = TextBlob(row["Overview"]).sentiment.polarity
        results.append((row["Series_Title"], row["Genre"], row["IMDB_Rating"], pol))

    return results

def show(recs, name):
    print(Fore.YELLOW + f"\nMovie Recommendations for {name}:\n")

    for i, (title, genre, rating, pol) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. {title}")
        print(f"   Genre: {genre}")
        print(f"   IMDB Rating: {rating}")
        print(f"   Sentiment: {pol:.2f} ({senti(pol)})\n")

def get_genre():
    print(Fore.GREEN + "Available Genres:")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.CYAN}{i}. {g}")

    while True:
        x = input(Fore.YELLOW + "Enter genre number or name (or skip): ").strip()

        if x.lower() == "skip":
            return None

        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]

        x = x.title()
        if x in genres:
            return x

        print(Fore.RED + "Invalid input. Try again.\n")

def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()

        if x.lower() == "skip":
            return None

        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            print(Fore.RED + "Rating out of range.\n")
        except:
            print(Fore.RED + "Invalid input.\n")

print(Fore.BLUE + "Movie Recommendation Assistant\n")

name = input(Fore.YELLOW + "What's your name? ").strip()
print(Fore.GREEN + f"\nHello, {name}!\n")

print(Fore.BLUE + "Choose mode:")
print("1. Filter (Genre + Mood + Rating)")
print("2. Random")

mode = input(Fore.YELLOW + "Enter choice: ").strip()

if mode == "1":
    genre = get_genre()
    mood = input(Fore.YELLOW + "How do you feel today? ").strip()

    print("Analyzing mood", end="", flush=True)
    dots()

    mp = TextBlob(mood).sentiment.polarity
    print(Fore.GREEN + f"\nMood polarity: {mp:.2f}\n")

    rating = get_rating()

    print("Finding movies", end="", flush=True)
    dots()

    recs = recommend(genre, mood, rating)

elif mode == "2":
    print("Picking random movies", end="", flush=True)
    dots()
    recs = random_recommend()

else:
    print(Fore.RED + "Invalid choice.")
    raise SystemExit

if isinstance(recs, str):
    print(Fore.RED + recs)
else:
    show(recs, name)
