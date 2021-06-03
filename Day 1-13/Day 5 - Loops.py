import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = round(random.random()*100, 2)
randomnumS = str(randomnum)

'''
Loops

for x in list:
    #Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    
range(): Repeating a loop between a range, not including b
    for number in range(a, b, [step]):
        print(number)

for number in range(1, 10):
    print(number) = Prints from 1 to 9
    
for number in range(1, 11, 3):
    print(number) = Prints from 1 to 10 in steps of 3 (1, 4, 7, 10)

total = 0
for number in range(1, 101):
    total += number
print(total) = Ansuer is 5050

'''
"""
# Interactive Exercise #1
# 🚨 Don't change the code below 👇
#input().split(separator, maxsplit). When no separator, use space.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
mean_height = 0
divider = 0
for heights in student_heights:
    mean_height += heights
    divider += 1
mean = round(mean_height/divider)
print(mean)
"""
"""
# Interactive Exercise #2
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
"""
"""
# Interactive Exercise #3

total = 0
numbers = []
for n in range(2, 101, 2):
    total += n
    numbers.append(n)
print(total)
"""

"""
# Interactive Exercise #4
# It is easier and more efficient using "and" operator
for n in range(1, 101):
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")          
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)
"""

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_len = len(letters)
letters_counter = 0
chars = []
symbols_len = len(symbols)
symbols_counter = 0
syms = []
numbers_len = len(numbers)
numbers_counter = 0
nums = []
easy_password = ""
hard_password = ""

for letras in letters:
    if letters_counter == nr_letters:
        break
    easy_password += random.choice(letters)
    letters_counter += 1
    

for simbolos in symbols:
    if symbols_counter == nr_symbols:
        break
    easy_password += random.choice(symbols)
    symbols_counter += 1

for numeros in numbers:
    if numbers_counter == nr_numbers:
        break
    easy_password += random.choice(numbers)
    numbers_counter += 1
print(f"Your eazy password is: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_counter = 0
symbols_counter = 0
numbers_counter = 0
password = []
for letras in letters:
    if letters_counter == nr_letters:
        break
    chars.append(random.choice(letters))
    password.append(chars[letters_counter])
    letters_counter += 1

    

for simbolos in symbols:
    if symbols_counter == nr_symbols:
        break
    syms.append(random.choice(symbols))
    password.append(syms[symbols_counter])
    symbols_counter += 1


for numeros in numbers:
    if numbers_counter == nr_numbers:
        break
    nums.append(random.choice(numbers))
    password.append(nums[numbers_counter])
    numbers_counter += 1

random.shuffle(password)

final_counter = 0
for i in password:
    hard_password += password[final_counter]
    final_counter += 1
print(f"Your hardcore password is: {hard_password}")

# Also, the use of range makes the code a lot shorter:
"""
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
"""










