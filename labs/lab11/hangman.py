"""
Name: Steve Ford
hangman.py
"""

from random import randint


def make_list():
    # read word_bank.txt and compile it into a list
    # lowercase all words
    # call pick word with list

    word_bank = []
    file = open("Word_Bank.txt", "r")
    for line in file:
        word_bank.append(line.lower().removesuffix("\n"))
    return word_bank


def pick_word(words):
    # parameter is word bank compiled list, returns a singular string IE singular secret word
    selection = randint(0, len(words) - 1)
    return words[selection]


def display_progress(secret_word, guesses):
    # parameter is secret word + all guessed strings
    # compares guessed characters to modify the "progress string"
    # print progress string to screen
    # print number of guesses to screen
    # print what previous guesses have been made which are not in the secret to screen
    # return the progress string
    incorrect = []
    progress = ""
    for letter in secret_word:
        for i in range(len(guesses)):
            if guesses[i] == letter:
                progress += guesses[i]
                break
            elif i == len(guesses) - 1:
                progress += "_"
    for i in range(len(guesses)):
        for letter in secret_word:
            if guesses[i] == letter:
                break
            elif letter == secret_word[-1]:
                incorrect.append(guesses[i])

    print(progress)
    print("You have incorrectly guessed the following letters: ", incorrect)
    return progress


def is_correct(progress, secret_word):
    # parameter is secret word and progress string
    # returns true or false
    if progress == secret_word:
        return True
    return False


def play_game():
    # call make list which calls pick word which returns our secret word

    # assign secret word/store in a variable
    # initialize a list of guessed characters (7-length = remaining guesses)
    # initialize progress string

    # while not ! is_correct(secret, progress) is false enter game loop

    # if len(list) == 7
    # game is over, print secret + guesses, pause then run play_game()

    # game loop first asks for input of 1 character
    # only take input that is length 1
    # lowercase input
    # loop through list of guessed characters to verify it is a new entry
    # append input to list of guessed chars
    # call display progress() with secret word + list of guessed chars
    # assign the return to local progress string

    # down here means while loop is broken IE victory
    # display victory, pause, run play_game

    word_bank = make_list()
    secret_word = pick_word(word_bank)
    print(secret_word)
    guessed_chars = []
    progress_str = ""
    for _ in range(len(secret_word)):
        progress_str += "_"
    lives_acc = 0

    while not(is_correct(progress_str, secret_word)):
        print()
        print("You have ", str(7 - lives_acc), " guesses remaining")

        if lives_acc >= 7:
            print("GAME OVER!!! The secret word was: ", secret_word)

            print("Press any key to restart...")
            input()
            play_game()

        guess = str(input("Guess a letter: "))
        if len(guess) == 1:
            guess = guess.lower()
            for i in range(len(guessed_chars)):
                if guessed_chars[i] == guess:
                    break
                elif i == len(guessed_chars) - 1:
                    guessed_chars.append(guess)
                    new_progress_str = display_progress(secret_word, guessed_chars)
                    if new_progress_str == progress_str:
                        lives_acc += 1
                    else:
                        progress_str = new_progress_str
            if len(guessed_chars) == 0:
                guessed_chars.append(guess)
                new_progress_str = display_progress(secret_word, guessed_chars)
                if new_progress_str == progress_str:
                    lives_acc += 1
                else:
                    progress_str = new_progress_str
        else:
            print("Only enter 1 letter at a time!")
            print()

    print("You WON!!!")
    print("Press any key to restart...")
    input()
    play_game()


def main():
    play_game()


main()
