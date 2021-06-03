import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = random.randint(10, 99)
"""
# Today class is all about numbers, operations and pretty much everything
# related to calculation. The project is a tip calculator that divides the
# a total input bill, between how many will the bill be split, percentage
# of the tip and finally our calculation.
"""
print("Day 2\n")
"""
Introducing attributes:
    
    string: Normal text, like the one we use in our print() function.
            always concatenated between ""
    int: Entire numbers, or -2, -1, 0, 1, 2, and so on. No decimals
    float: Floating point number. Now we enter the world of decimals!
            3.1416 or Pi is a float
    boolean: True or false. It is as easy as it can get.
    
Attributes can be converted between each other, be it a user-created function
or basic functions like "len()". len() only accepts a container, or string,
counting the total of characters of this container and returning a result
with attribute int. That's why len() returns an exception (error) when 
you input an int. "123" is treated like a string, not an int, opposed to 
123. Common convertion functions:
    int() = String to integer
    str() = int to string
    float() = String to float
    type() = 
    
type() can also be used to check the attribute of a container
    
Strings can be used with "subscripts". That means, a value of my 
whole string to be printed. For example, the word "Hello", where H is 
the subscript 0, and O is the subscript 4. Programation Languages always 
start counting from 0, so it's pretty important to take that into account.

A number written like 123_456_789 = 123456789.

Arithmetic Operators:
    Addition = +
    Subtraction = -
    Multiplication = *
    Division = / (float result)
    Division = // (int result)
    Power = **
    
    Further manipulation of variables: 
    += : Adds the specified value (after =) to the variable (before +)
    This can be used with -, *, /, **. Useful for modifying variables in
    conditionals or functions.
    
f-string:
    We can mix variables with different attributes without converting:
    score = 0
    height = 1.8
    isWinning  = True
    print(f"your score is {score}, your height is {height}, and are you winning? {isWinning}")
    
"""
print("Hello"[4])
# Anothe example of subscript
street_name = "Abbey Road"
print(street_name[4] + street_name[7] +"\n")

print("Interactive task #1:\n")

# 🚨 Don't change the code below 👇
two_digit_number = str(randomnum)
print("Your 2 digit number is: " + two_digit_number)
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
number1 = int(two_digit_number[0])
number2 = int(two_digit_number[1])
print(number1+number2)

print("\nInteractive task #2:\n")

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# The equation for BMI is weight/height^2

height_int = float(height)
weight_int = float(weight)
BMI = weight_int/(height_int**2)
# round() can be used to round to how many decimal places I want. Use 
# second argument for that. e.g. round(17.6536546, 2)= 17.65
BMI_int = round(BMI)
print(BMI_int)

print("\nInteractive task #3:\n")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
inputage = int(age)
age_int = 90-inputage
months = age_int*12
days = age_int*365
weeks = age_int*52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print("Day 2 Project:\n")
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to our tip calculator. Type the total value of the bill, the amount of people and the percentage and we'll do the calculation for you:\n")
bill_str = input("What was the total bill?: $")
people_str = input("How many people to split the bill?: ")
percentage_str = input("What percentage tip would you like to give? 10, 12 or 15?: ")

bill = float(bill_str)
people = float(people_str)
percentage = int(percentage_str)/100

tip = round((bill/people)*(1+percentage), 2)

print(f"Each person should pay: ${tip}")

