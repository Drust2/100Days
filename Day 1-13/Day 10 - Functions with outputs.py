import random
import sys
#-*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 10 - Functions with outputs

def my_function():
    result = 3 * 2
    return result

This function will return the variable that we design with "return" keyword

#Change the name to Title case
def format_name(first_name, last_name):
    f_name = first_name.title()
    l_name = last_name.title()
    output = f_name + " " + l_name
    return output

The return line is the end of the function and will make the code exit it.
Nothing is going to be read after a return line. That creates the possibility
for an "early return". You can write return to exit the function early. This
is useful when e.g. an input is not valid.
"""
def format_name(first_name, last_name):
    """
    

    Parameters
    ----------
    first_name : First name to be capitalized. -> str
    last_name : Last name to be capitalized. -> str

    Returns
    -------
    output : Capitalized versions of each string -> str

    """
    f_name = first_name.title()
    l_name = last_name.title()
    output = f_name + " " + l_name
    return output

format_name("JUAN", "rodriguez")

#Interactive Exercise 1

#Functions of the calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

math_operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}  

#Main function of the program.
def calculator():
  #Function that realizes the calculation
  def calculation(n1, n2):
    checker = 0
    for operation in math_operations:
        if arithmetic_symbol == operation:
            checker = 1

    if checker == 0:
        sys.exit("Please try again with a correct input.")
    
    function = math_operations[arithmetic_symbol]
    return function(n1, n2)

  #Creating the main loop
  stop_calculator = False

  #User inputs
  num_1 = float(input("Enter the first number: "))
  num_2 = float(input("Enter the second number: "))

  #Printing the symbols
  for operations in math_operations:
    print(operations)

  #Arithmetic operator selection
  arithmetic_symbol = input("Pick an operation from the line above to proceed: ")

      
  #Result of the first calculation
  result = calculation(num_1, num_2)
  print(f"{num_1} {arithmetic_symbol} {num_2} = {result}")

  while stop_calculator == False:
    #Check if the user wants to continue
    user_continues = input(f"Type y to continue calculating with {result} or n to start again: ").lower()

    if user_continues == "n":
      stop_calculator = True
      calculator()

    else:
      num_1 = result
      arithmetic_symbol = input("Pick another operation: ")
      num_2 = float(input("Enter the second number for the operation: "))
      result = calculation(result, num_2)
      print(f"{num_1} {arithmetic_symbol} {num_2} = {result}")

calculator()