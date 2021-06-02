# -*- coding: utf-8 -*-
import time
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day - 15 IDEs
"""
#Constants
QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01

#Available options. Liquids are in mililiters (ml), money in $ and coffee in grams (g)
drinks = [
    {
     "name": "Espresso",
     "cost": 1.50,
     "water": 50,
     "coffee": 18,
     "milk": 0,
    },    
    {
     "name": "Latte",
     "cost": 2.50,
     "water": 200,
     "coffee": 18,
     "milk": 150,
    },    
    {
     "name": "Cappuccino",
     "cost": 3.00,
     "water": 250,
     "coffee": 24,
     "milk": 100,
    }
]

#Status of the machine
status = {
    "water": 300,
    "milk": 200,
    "coffee": 76,
    "money": 0,
    }

#Check if there are enough resources in the machine for the selected beverage
def check_products(drink):
    for i in drinks:
            if i["water"] > status["water"] and drink == i["name"]:
                print("\n-----------------------------------------------------------------------------")
                print(f"\nNot enough water in the machine to brew {drink}.")
                print("\n-----------------------------------------------------------------------------\n")
                time.sleep(2)
                return True
            if i["milk"] > status["milk"] and drink == i["name"]:
                print("\n-----------------------------------------------------------------------------")
                print(f"\nNot enough milk in the machine to brew {drink}.")
                print("\n-----------------------------------------------------------------------------\n")
                time.sleep(2)
                return True
            if i["coffee"] > status["coffee"] and drink == i["name"]:
                print("\n-----------------------------------------------------------------------------")
                print(f"\nNot enough coffee in the machine to brew {drink}.")
                print("\n-----------------------------------------------------------------------------\n")
                time.sleep(2)
                return True
        
#Buy the drink
def buy(drink, q, d, n, p):
    """
    Parameters
    ----------
    selection : Beverage selected.
    q : Amount of Quarters inserted.
    d : Amount of Dimes inserted.
    n : Amount of Nickles inserted.
    p : Amount of Pennies inserted.

    Returns
    -------
    change : Change of the transaction. -> int

    """
    payment = (QUARTER*q + DIME*d + NICKEL*n + PENNY*p)
    change = 0
    for i in drinks:
        if payment < i["cost"] and drink == i["name"]:
            print("\nNot enough money inserted. Refunding.")
            return -1        
        if drink == i["name"]:
            status["water"] -= i["water"]
            status["milk"] -= i["milk"]
            status["coffee"] -= i["coffee"]
            status["money"] += i["cost"]
            change = payment - i["cost"]
    return change

#Main loop of the machine
turn_off = False
while not turn_off:
    print("\nWhich beverage would you like?:\n")
    print(" a. Espresso - $1.50 \n b. Latte - $2.50 \n c. Cappuccino - $3.00")
    user_prompt = input("Type the corresponding letter (a, b or c) for your choice: ").lower()
    
    #Turn off the machine
    if user_prompt == "off":
        turn_off = True
        print("Turning off...")
        
    #Print report
    elif user_prompt == "report" or user_prompt == "status":
        print("-----------------------------------------------------------------------------")
        print("\nCoffee Machine current status:")
        print(f" Water: {status['water']}ml\n Milk: {status['milk']}ml\n Coffee: {status['coffee']}g\n Money: ${status['money']}\n")
        print("-----------------------------------------------------------------------------\n")
        time.sleep(3)
    #User choice or incorrect input
    else:
        if user_prompt != "a" and user_prompt != "b" and user_prompt != "c":
            print("-----------------------------------------------------------------------------\n")
            print("Invalid input entered.\n")
            print("-----------------------------------------------------------------------------\n")
            time.sleep(2)
        else:
            beverage = ""
            if user_prompt == "a":
                beverage = "Espresso"
            elif user_prompt == "b":
                beverage = "Latte"
            elif user_prompt == "c":
                beverage = "Cappuccino"
            not_enough = check_products(beverage)
                
            if not not_enough:
                print("\nPlease insert the coins.\n")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                change = round(buy(beverage, quarters, dimes, nickles, pennies),2)
                if change != -1:
                    print("\nPreparing...\n")
                    time.sleep(5)
                    print(f"\nHere's ${change} in change.")
                    print(f"Enjoy your {beverage} ☕.")
                    print("-----------------------------------------------------------------------------")
                    time.sleep(1)
                
            
