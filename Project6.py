import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

try:
    df = pd.read_csv("imdb_top_1000.csv")
except:
    print(Fore.RED + "File not found!")
    exit()

genres = sorted(set(",".join(df["Genre"].dropna()).split(", ")))

def dots():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return polarity, "Positive 😊"
    elif polarity < 0:
        return polarity, "Negative 😞"
    else:
        return polarity, "Neutral 😐"

def recommend_movies(genre=None, mood=None, rating=None, n=5):
    data = df

    if genre:
        data = data[data["Genre"].str.contains(genre, case=False, na=False)]

    if rating:
        data = data[data["IMDB_Rating"] >= rating]

    if data.empty:
        return []

    data = data.sample(frac=1)

    results = []

    for _, row in data.iterrows():
        overview = row["Overview"]
        if pd.isna(overview):
            continue

        polarity, senti = get_sentiment(overview)

        if mood:
            if "happy" in mood.lower() and polarity < 0:
                continue
            if "sad" in mood.lower() and polarity > 0:
                continue

        results.append({
            "title": row["Series_Title"],
            "genre": row["Genre"],
            "rating": row["IMDB_Rating"],
            "sentiment": senti,
            "polarity": polarity
        })

        if len(results) == n:
            break

    return results

def show_movies(movies, name):
    print(Fore.YELLOW + f"\n🎬 Recommendations for {name}:\n")

    for i, m in enumerate(movies, 1):
        print(Fore.CYAN + f"{i}. {m['title']}")
        print(f"   Genre: {m['genre']}")
        print(f"   Rating: {m['rating']}")
        print(f"   Sentiment: {m['sentiment']} ({m['polarity']:.2f})\n")

print(Fore.BLUE + "🎥 Movie Recommendation System 🎥\n")

name = input("Enter your name: ")
print(Fore.GREEN + f"Hello {name}!\n")

mode = input("Choose recommendation type (ai/random): ").lower()

print("\nAvailable Genres:")
for i, g in enumerate(genres, 1):
    print(f"{i}. {g}")

g_choice = input("\nEnter genre (or press Enter to skip): ").strip()
genre = g_choice if g_choice else None

mood = None
if mode == "ai":
    mood = input("How are you feeling? (happy/sad/anything): ")

r_input = input("Minimum rating (or press Enter to skip): ").strip()
rating = float(r_input) if r_input else None

print(Fore.BLUE + f"\nMode Selected: {mode.upper()} Recommendation\n")

print("Finding movies", end="")
dots()

movies = recommend_movies(genre, mood, rating)

if not movies:
    print(Fore.RED + "No movies found.")
else:
    show_movies(movies, name)

while True:
    again = input("Want more recommendations? (yes/no): ").lower()

    if again == "yes":
        movies = recommend_movies(genre, mood, rating)
        show_movies(movies, name)
    elif again == "no":
        print("Goodbye! 🎬")
        break
    else:
        print("Invalid input.")
