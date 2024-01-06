import random

def fortune_teller():
    print("Welcome to the Python Fortune Teller!")
    input("Think of a question and press Enter to reveal your fortune...")

    fortunes = [
        "The stars say yes!",
        "It is certain.",
        "Reply hazy, try again.",
        "Don't count on it.",
        "Outlook not so good."
    ]

    # Randomly select a fortune
    selected_fortune = random.choice(fortunes)

    print("\nYour fortune is:")
    print(selected_fortune)

if __name__ == "__main__":
    fortune_teller()
