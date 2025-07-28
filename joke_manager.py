import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

JOKES_FILE = "jokes.txt"

def load_jokes():
    try:
        with open(JOKES_FILE, "r") as file:
            jokes = file.read().splitlines()
    except FileNotFoundError:
        jokes = []
    return jokes

def save_joke(new_joke):
    with open(JOKES_FILE, "a") as file:
        file.write(new_joke + "\n")

def show_random_joke(jokes):
    if jokes:
        joke = random.choice(jokes)
        print(Fore.CYAN + "\nHere’s your programming joke:\n")
        print(Fore.YELLOW + joke)
    else:
        print(Fore.RED + "\nNo jokes found. Add one first!")

def main():
    jokes = load_jokes()

    while True:
        print(Fore.GREEN + "\n🐍💡 Programming Jokes Menu:")
        print(Fore.GREEN + "1. Get a random joke")
        print(Fore.GREEN + "2. Add a new joke")
        print(Fore.GREEN + "3. Exit")

        choice = input(Fore.BLUE + "Choose an option (1/2/3): ")

        if choice == "1":
            show_random_joke(jokes)
        elif choice == "2":
            new_joke = input(Fore.MAGENTA + "\nType your new joke: ")
            save_joke(new_joke)
            jokes.append(new_joke)
            print(Fore.GREEN + "✅ Joke saved!")
        elif choice == "3":
            print(Fore.CYAN + "Goodbye! Keep laughing! 😂")
            break
        else:
            print(Fore.RED + "Invalid option. Try again!")

if __name__ == "__main__":
    main()
