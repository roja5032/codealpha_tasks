import random

# Step 1: word list
words = ["python", "computer", "science", "hangman", "programming"]
secret_word = random.choice(words)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")

# Step 2: game loop
while tries > 0:
    # Display current word with underscores
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("\nWord:", display_word)

    # Win condition
    if display_word == secret_word:
        print("🎉 You guessed it! The word was", secret_word)
        break

    # Ask user for a guess
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that!")
    elif guess in secret_word:
        print("Good guess!")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        tries -= 1
        print("Tries left:", tries)

# Lose condition
if tries == 0:
    print("😢 Game over! The word was:", secret_word)

