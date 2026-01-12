import random

# My first GitHub App

# A list of quotes to choose from
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your passion is waiting for your courage to catch up. - Isabelle Lafleche",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Stay hungry, stay foolish. - Steve Jobs"
]

def show_motivation():
    # Pick one random quote from the list
    daily_quote = random.choice(quotes)
    print("\n--- DAILY MOTIVATION ---")
    print(daily_quote)
    print("------------------------\n")

if __name__ == "__main__":
    show_motivation()