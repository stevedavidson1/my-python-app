import random

# Version 2.0: Personalizing the motivation
quotes = [
    "Believe you can and you're halfway there.",
    "The best way to predict the future is to invent it.",
    "Stay hungry, stay foolish."
]

def show_motivation():
    name = input("Enter your name for a custom quote: ")
    daily_quote = random.choice(quotes)
    
    print(f"\n--- {name.upper()}'S DAILY MOTIVATION ---")
    print(daily_quote)
    print("--------------------------------------\n")

if __name__ == "__main__":
    show_motivation()