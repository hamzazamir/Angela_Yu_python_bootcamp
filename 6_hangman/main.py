import random
from ascii_art import stages, logo
from hangman_words import word_list


word_list = word_list
random_word = random.choice(word_list)
random_word_length = len(random_word)
end_of_game = False
number_of_lives = 6

print(logo)

display = []

for _ in range(random_word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(random_word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in random_word:
        print(f"You guessed {guess}, that's not in the word you lose a life. ")
        number_of_lives -= 1
        if number_of_lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You Win!!")

    print(stages[number_of_lives])
