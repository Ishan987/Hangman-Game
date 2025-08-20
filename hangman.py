import random

# Words list
words = ["python", "hangman", "developer", "computer", "programming", "artificial", "intelligence"]

# Hangman stages
stages = [
    """
       --------
       |      |
       |      
       |    
       |     
       |     
    """,
    """
       --------
       |      |
       |      O
       |    
       |     
       |     
    """,
    """
       --------
       |      |
       |      O
       |      |
       |     
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |     
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
    """
]

# Choose random word
word = random.choice(words)
word_letters = set(word)
guessed_letters = set()
lives = len(stages) - 1

print("=== Welcome to Hangman ===")

while len(word_letters) > 0 and lives > 0:
    print(stages[len(stages) - 1 - lives])
    print("Lives left:", lives)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

    # Display current progress
    current_word = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(current_word))

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
    else:
        lives -= 1
        print("Wrong guess!")

# Final result
if lives == 0:
    print(stages[-1])
    print(f"Game Over! The word was '{word}'.")
else:
    print(f"Congratulations! You guessed the word '{word}'!")
