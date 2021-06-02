import art
from game_data import data
import random

#Variables
famous_1 = random.choice(data)
famous_2 = random.choice(data)

#While loop to avoid both dictionaries being the same.
while famous_2 == famous_1:
	famous_2 = random.choice(data)

#Info of both dictionaries
famous_1_name = famous_1["name"]
famous_1_followers = famous_1["follower_count"]
famous_1_description = famous_1["description"]
famous_1_country = famous_1["country"]

famous_2_name = famous_2["name"]
famous_2_followers = famous_2["follower_count"]
famous_2_description = famous_2["description"]
famous_2_country = famous_2["country"]

#Functions

#Function that compares the answer of the player and adds returns 1 if correct or -1 if incorrect to end the game
def comparation(answer):
	if answer == "a":
		if famous_1_followers > famous_2_followers:
			return 1
		else:
			return -1
	else:
		if famous_2_followers > famous_1_followers:
			return 1
		else:
			return -1

#Main function of the game
def game():
	print(art.logo)
	print("Who has the most followers on Instagram?\n")
	print(f"{famous_1_name}, {famous_1_description}, from {famous_1_country}")
	print(art.vs)
	print(f"{famous_2_name}, {famous_2_description}, from {famous_2_country}")
	
	#Ask the user from prompt A or B. Encased in a while for incorrect prompts
	player_answer = "c"
	while player_answer != "a" and player_answer != "b":
		player_answer = input(f"Type 'a' for {famous_1_name} or 'b' for {famous_2_name}: ").lower()

game()

