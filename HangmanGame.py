import random

def hangman():
    words = ["python", "hangman", "programming", "challenge", "computer", "developer"]
    selected_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_display = ['_' for _ in selected_word]

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses and '_' in word_display:
        print("\nCurrent word: " + ' '.join(word_display))
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print("Guessed letters: " + ', '.join(guessed_letters))

        guess = input("Please guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            for index, letter in enumerate(selected_word):
                if letter == guess:
                    word_display[index] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Sorry, that letter is not in the word.")

    if '_' not in word_display:
        print("\nCongratulations! You've guessed the word: " + selected_word)
    else:
        print("\nGame over! The word was: " + selected_word)

if __name__ == "__main__":
    hangman()
