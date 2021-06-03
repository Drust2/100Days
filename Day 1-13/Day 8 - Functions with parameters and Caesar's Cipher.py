import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = round(random.random()*100, 2)
randomnumS = str(randomnum)
"""
Day 8 - Function Parameters & Caesar Cipher

def my_function(something):
    #Do this with something
    #Then do this
    #Finally do this
    
    Example:
        def word_printer(word):
            print(f"Are you trying to print {word}? You did it!")
            
        word_printer("Esta función imprime lo que sea!")
        
    #Function with more than 1 input. Positional arguments, they have an order!
    def my_function(a, b, c):
        #Do this with a
        #Then do this with b
        #Finally do this with c
        
    def greet_with(name, location):
        print(f"Greetings from {location}. Nice to meet you, my name is {name}")

    greet_with("Deivid", "Antartica")
    
    #Keyword Arguments: Now the arguments don't need a specified order
    def my_function(a=1, b=2, c=3):
        #Do this with a
        #Then do this with b
        #Finally do this with c
    
    greet_with(name = "Angela", location = "London"):
        print(f"Greetings from {location}. Nice to meet you, my name is {name}")
"""
# Interactive Exercise 1

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
  result = math.ceil((height*width)/cover)
  print(result)


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Interactive Exercise 2

#Write your code below this line 👇
'''
prime = []
def prime_checker(number):
  if number == 2 or number == 3 or number == 5 or number == 7:
    print(f"{number} is prime")
    prime.append(number)
  else:
    res_1 = number%2
    res_2 = number%3
    res_3 = number%5
    res_4 = number%7
    results = [res_1, res_2, res_3, res_4]
    if 0 in results:
      print(f"{number} is not prime")
    else:
      print(f"{number} is prime")
      prime.append(number)
      
for i in range(100):
  prime_checker(i)

print(prime)
'''

#Better form
def prime_checker(number):
  is_prime = True
  for i in range(2, number-1):
    if number%i == 0:
      is_prime = False
  if not is_prime:
    print("The number is not prime")
  else:
    print("The number is prime")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

letter = "a"

# Project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
  alphabet_length = len(alphabet)
  counter = 0
  encrypted_word = list(text)
  encription = ""
  for charac in text:
    indexchar = alphabet.index(encrypted_word[counter])
    new_index = indexchar+shift
    
    if new_index > alphabet_length-1:
      adjusted = new_index - alphabet_length
      encrypted_word[counter] = alphabet[adjusted]
      encription += encrypted_word[counter]
      counter += 1
      
    else: 
      change = alphabet[new_index] 
      encrypted_word[counter] = change
      encription += encrypted_word[counter]
      counter += 1
  
  print(f"The encoded text is {encription}")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == 'encode':
  encrypt(text, shift)
