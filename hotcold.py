import random
from display import *

def guess_game():
    is_guess_game = True
    is_guess_game2 = True
    number = random.randint (1, 666)
    guesses_taken = 0
    guess = 0
    print("I am the master of the labirynth. Solve my mystery od die!")
    print("I am thinking of a number between 1 and 666")
    while is_guess_game:
        while is_guess_game2:
            try:
                if guess is not 0:
                    print("Your last guess: " + str(guess))
                print(import_sprite('sphinx_sprite'))
                print("You guessed " + str(guesses_taken) + " times")
                guess = int(input("Enter your number: "))
                os.system('clear')
                guesses_taken += 1
                is_guess_game2 = False
            except ValueError:
                os.system('clear')
                print("It's not even a number")
                is_guess_game2 = True
        if guess < number:
            if abs(number - guess) < 10:
                print("Oof, that's hot")
            elif abs(number - guess) > 10:
                print("That's cold my dude")
            print("Your guess is too low")
        elif guess > number:
            if abs(number - guess) < 10:
                print("Oof, that's hot")
            elif abs(number - guess) > 10:
                print("That's cold my dude")
            print("Your guess is too high")
        else:
            win_screen()
        if guesses_taken > 10:
            lose_screen()

        is_guess_game2 = True
        