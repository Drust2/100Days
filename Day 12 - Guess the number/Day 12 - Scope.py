from sys import exit
# -*- coding: utf-8 -*-
#cls = lambda: print("\033[2J\033[;H", end='')
#cls()
"""
Day 12 - Scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

Variable "enemies" is 1 outside the function but 2 inside it, no matter if the function changes it. This is a scope:
    
    #Local Scope
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
    #I can't call a variable from outside a function if it's defined outside. That means it is only valid inside the function.
    drink_potion()
    print(potion_strength)

    #Global Scope
    #Here we have a variable that is global to all functions, as it's defined at the top level.
    player_health = 10
    
     def drink_potion():
        potion_strength = 2
        print(player_health)
    
    drink_potion()

#There is no block scope in Python: Ifs, whiles, etc, don't create a local scope. 

Using the Keyword 'global', one can call a global variable inside a function

enemies = 1

def increase_enemies():
  global enemies += 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global constants: Useful with the 'global' keyword. The convention is to write them all in caps lock

"""

#Project 12 - Guess the number
from logo import logo
import random

#Variables & Constants
EASY = 10
HARD = 5
answer = random.randint(1, 100)
remaining_guesses = 0

#Functions

#Function that compares the number
def check_answer(guess):
    """
    Parameters
    ----------
    guess : Input of the player 

    Returns
    -------
    bool
        Returns True or False depending if the answer is correct or not

    """
    if guess > answer:
        print("You're too high.")
        return False
    elif guess < answer:
        print("You're too low.")
        return False
    elif guess == answer:
        print(f"You're right! {guess} was the number!")
        return True

#Main function of the game
def game():
    cls = lambda: print("\033[2J\033[;H", end='')
    cls()
    print(logo)
    #Variable that ends the loop or finishes the game if the answer is right
    right_answer = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'll think of a number between 1 and 100 and your task is to guess it.")
    print(f"Can you keep a secret? The number is {answer}. Don't tell anyone!")
    print("First of all, we need to choose a difficulty.")
    
    difficulty = input("Type 'easy' or 'hard' to choose: ").lower()
    #Check the difficulty of the game and give the assigned lives
    if difficulty == "easy":
        remaining_guesses = EASY
    elif difficulty == "hard":
        remaining_guesses = HARD
    else:
        print("Incorrect input. It's not nice messing with computers! You need to restart the code.")
        return
    #Loop that continues the game until the player runs out of guesses
    while remaining_guesses > 0 and right_answer == False:
        print((f"You have {remaining_guesses} attempts remaining to guess the number."))
        player_guess = int(input("Try a number!: "))
        right_answer = check_answer(player_guess)
        
        #Checks the answer
        if right_answer == False:
            remaining_guesses -= 1
            if remaining_guesses == 0:
                print(f"You're out of guesses. The answer was {answer}. Better luck next time!")

    #Ask if the user wants to play again
    play_again = input("Do you want to play again? Type 'y' for yes or 'n' to exit: ").lower()
    if play_again == 'y':
        game()
    else:
        print("Bye!")
        return
    
game()








