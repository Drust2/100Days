import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 9 - Python Dictionaries

{Key: Value} - Creation of a dictionary. 
Keys are, for example in a real dictionary - Bug, function or loop
where it's value is the definition of Bug.

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#Printing the dictionary for the key "Bug". The key must be spelled correctly.
print(programming_dictionary["Bug"])

#Adding new entries to the dictionary.
programming_dictionary["Value"] = "The definition of a key in a dictionary."

#Creating an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}

#Edit an entry in the dictionary
programming_dictionary["Bug"] = "Hey, it's not nice to change definitions."

#Looping through a dictionary
for key in programming_dictionary:
    print(key) - Printing the key
    print(programming_dictionary[key]) - Printing the value
    
#Nesting Lists and dictionaries:
{
    Key:[List],
    Key2:{Dict},
}

capitals = {
    "France": "Paris"
    "Germany": "Berlin".
}

travel_log = 
    {
    "France": 
        {
            "cities_visited": ["Paris", "Lille", "Dijon"],
            "total_visits": 12},
    
    "Germany": 
        {
            "cities_to_visit": ["Berlin", "Hamburg", "Stuttgart"],
            "cities_visited": ["Münschen", "Oldenburg", "Köln"],
            "total_visits": 5,
        }
}

#Nesting Dictionary in a List
travel_log_list = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
    },    
    {
     "country": "Germany", 
     "cities_visited": ["Münschen", "Oldenburg", "Köln"],
     "total_visits": 5,
    }
]

"""
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
'''
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
  travel_log.append(
    {
      "country": country_visited,
      "visits": times_visited,
      "cities": cities_visited,
    }
  )

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
'''
#HINT: You can call clear() to clear the output in the console.

#Creating a blank list for all the players
bid_participant = []

#Function that adds a participant to the dictionary
def add_participant(name_of_player, bid_of_player):
  bid_participant.append(
    {
      "Name": name_of_player,
      "Bid": bid_of_player,
    }
  )
#Variable that controls the loop to add more players
no_more_players = False

#Input that controls the game
while not no_more_players:
  input_name = input("What is your name?: ")
  input_bid = input("What is your bid?: ")
  add_participant(name_of_player=input_name, bid_of_player=input_bid)
  another_player = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  if another_player == 'yes':
    #clear()
    input_name = ""
    input_bid = ""
  else:
    no_more_players = True

winner_bid = 0
winner_name = ""

for player in range(len(bid_participant)):
  control_name = bid_participant[player]["Name"]
  control_bid = int(bid_participant[player]["Bid"])
  if winner_bid < control_bid:
    winner_bid = control_bid
    winner_name = control_name

print(f"The winner is {winner_name} with a bid of ${winner_bid}")












