import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = round(random.random()*100, 2)
randomnumS = str(randomnum)
"""
Day 7 - Hangman Project

IMPORTANT: A String behaves like a list of it's characters (chars). So, in a
for loop:
    for letter in "Kalamari Island":
        print(letter)
will go letter by letter doing a print. It is shorter than using "in range".

My Flowchart: 
    1. There's a list of words, that the program randomly chooses
    2. The program generates the drawing and the field of the chosen word
    3. The user is asked to guess a letter:
        a. They guess correctly - The letter gets added to the corresponding field.
        b. They guess wrong - We get a body part of the hangman and we lose a life.
    4. The user is asked again until they guess the word or losses all their lifes.
    
"""

# Interactive exercise 1

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
user_input = input("Please guess a letter: ")
guess = user_input.lower()

word_length = len(chosen_word)

for check in range(word_length):
  if guess == chosen_word[check]:
      print("Right")
  else:
      print("Wrong")
