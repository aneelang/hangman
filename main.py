import random
from hangman_wordlist import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)

end_of_game = False

# TODO: 1. Create an empty list called display
# For each letter in the chosen_word, add a "_" to display.
# So if the chosen word was "apple", display should be ....
display = []
for letter in chosen_word:
    display += '_'
print(display)


# TODO: 2. Loop through each position in the chosen word.
# if the letter at that position matches "guess" then append
# that letter to display


def check_the_word(val, lives):
    global end_of_game
    for pos in range(len(chosen_word)):
        if val == chosen_word[pos]:
            display[pos] = val
    if val not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print("You lose.")
            return -1
    print(stages[lives])
    return lives


def main():
    lives = 7
    guess_list = []
    global end_of_game
    # TODO: 3. Use a while loop to let the user guess again.
    # The loop should only stop once the user has guessed all the letters
    # in the chosen_word and 'display' has no more blanks "_". Then you can
    # tell the user they've won.
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in guess_list:
            print(f"You have already chosen {guess}")
            continue
        guess_list.append(guess)
        lives = check_the_word(guess, lives)
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You Won!")
            return
    print(f"The word was {chosen_word}")


if __name__ == "__main__":
    main()








