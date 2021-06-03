# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:09:18 2020

@author: rkn_d
"""
""
cls = lambda: print("\033[2J\033[;H", end='')
cls()
""
print("1st Interactive Exercise:\n")
print("Day 1 - Python Print Function\nThe function is declared like this\nprint('what to print')\n")

"""
Usage of indentations to be able to write lines with more elegance
print("Hello" + " " + "Angela\n")
"""
print("2nd Interactive Exercise:\n")
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " '"+"' " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n")

"""
Usage of input() function, that lets the user to input a string to be read
by the program:     
input("What is your name?\n")
"""
print("3rd Interactive Exercise:\n")
print("For seeing what we've done, just remember to remove the comments")

#print(len(input("Enter your name and the program will calculate its length:\n")))


"""
Usage of variables for... well everything. Objects are much better for 
handling the program like a champ. Let's redo the last exercise with a
variable:

print("Enter your name and the program will calculate its length:\n") 
yourName = input()
length = len(yourName)
print(length)

"""


print("\n4th Interactive Exercise:\n")
print("For seeing what we've done, just remember to remove the comments")
"""
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

new_a = b
new_b = a
a = new_a
b = new_b

#or c = a; a = b; b = c.



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
"""

print("\nDay 1 Project:\n")
print("Welcome to our deep complex Band Name Generator program v1.0")
print("You'll be asked a pair of personal questions and we'll select, based on your answers, a suitable name.")
print("First of all, tell us the city where you grew up in:\n")
city = input()
print("Now, tell us the name of a pet or animal you love:\n")
animal = input()
print("Excellent, your band name will be: " + city + " " + animal)



