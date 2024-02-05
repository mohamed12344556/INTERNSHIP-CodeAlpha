import random

def random_word():
    words = ["python", "hangman", "game", "computer", "cyber", "developer", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = random_word()
    attempts = 0

    print("Welcome to Hangman Game >_<")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                attempts += 1
                print(f"Wrong guess! Attempts left: {max_attempts - attempts}")
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You've guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
