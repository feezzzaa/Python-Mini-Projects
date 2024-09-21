import random

# Predefined list of words
WORDS = ['banana', 'apple', 'orange', 'grape', 'pineapple', 'watermelon', 'kiwi', 'strawberry']

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to select difficulty and attempts
def select_difficulty():
    print("Select Difficulty Level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        return 10
    elif choice == '2':
        return 6
    elif choice == '3':
        return 4
    else:
        print("Invalid choice, defaulting to Medium difficulty.")
        return 6

# Function to play one round of the Hangman game
def play_game():
    word = random.choice(WORDS)  # Randomly choose a word from the list
    attempts_left = select_difficulty()
    guessed_letters = set()  # Set of guessed letters
    wrong_guesses = set()  # Set of wrong guesses
    game_over = False

    print("\nWelcome to Hangman!")
    print(display_word(word, guessed_letters))  # Display the initial hidden word

    while not game_over:
        print(f"\nAttempts remaining: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Input validation for guessing
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single alphabetic letter.")
            continue
        elif guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            print(f"Wrong guess! The letter '{guess}' is not in the word.")
            wrong_guesses.add(guess)
            attempts_left -= 1

        print(display_word(word, guessed_letters))  # Display current word state

        # Check win/loss conditions
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}'.")
            game_over = True
        elif attempts_left == 0:
            print(f"Game over! You've run out of attempts. The word was '{word}'.")
            game_over = True

# Function to check if the player wants to play again
def play_again():
    choice = input("\nDo you want to play again? (y/n): ").lower()
    return choice == 'y'

# Main game loop
def main():
    print("Welcome to the Hangman Game!")

    while True:
        play_game()
        if not play_again():
            print("Thanks for playing! Goodbye.")
            break

# Start the game
if __name__ == "__main__":
    main()
