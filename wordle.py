import os
import config as cfg
from random import randint

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

with open(cfg.words_path) as file:
    words = file.read().split('\n')

words_count = len(words)
random_word = words[randint(0, words_count - 1)]

clear()

board = []
guess = input("Welcome to Wordle, make your guess:\n")
tries = 1

def player_won():
    return guess == random_word

def player_lost():
    return tries >= cfg.max_tries

def is_close(guess: str, index: int):
    letter = guess[index]

    if random_word[index] == letter:
        return False

    total_in_target = random_word.count(letter)

    used_for_green = sum(1 for i in range(len(random_word))
                         if guess[i] == letter and random_word[i] == letter)

    used_for_yellow = sum(1 for i in range(index) 
                         if guess[i] == letter and guess[i] != random_word[i] 
                         and guess[i] in random_word)

    remaining = total_in_target - used_for_green - used_for_yellow

    return remaining > 0

def print_word(word: str):
    status = [""] * len(random_word)
    for i, letter in enumerate(word):
        print("", letter, end=" ")
        if letter == random_word[i]:
            status[i] = cfg.symbols['correct']
        elif is_close(word, i):
            status[i] = cfg.symbols['exists']
        else:
            status[i] = cfg.symbols['incorrect']
    print()
    for s in status:
        print(s, end=" ")
    print()

def print_board():
    for word in board:
        print_word(word)

while True:
    if not (guess in words):
        guess = input("This is not a real word, please try again:\n")
        continue

    if len(guess) != len(random_word):
        guess = input("Please enter a valid string, guess again:\n")
        continue

    clear()
    board.append(guess)
    print_board()

    if player_won():
        print("You've guessed the word. Good job!")
        break
    elif player_lost():
        print(f"You've lost, the word was '{random_word}'.")
        break

    guess = input("Guess again: \n")
    tries += 1