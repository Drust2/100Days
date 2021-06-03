import random
import sys
#-*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Created on Wed Dec  2 11:06:48 2020

@author: rkn_d
"""

#Deck of the game
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Variables

#Blank list that contains the state of the game. Each player is contained inside as a dictionary.
player = "Human"
computer = "CPU"

current_game = []
current_game.append({
  "player": "Human",
  "current_hand": [],
})
current_game.append({
  "player": "CPU",
  "current_hand": [],
})
#Definition of all the functions relevant to the game

#Draws 2 cards for the player and adds them to the player dictionary. It returns the total hand of the player
def initial_draw_player():
    initial_count_player = 0
    Hu_C1 = random.choice(cards)
    Hu_C2 = random.choice(cards)
    if Hu_C1 == 11 and Hu_C2 == 11:
        Hu_C2 == 1

    current_game[0]["current_hand"].append(Hu_C1)
    current_game[0]["current_hand"].append(Hu_C2)
    hand_length = len(current_game[0]["current_hand"])
    for card in range(hand_length):
        initial_count_player += current_game[0]["current_hand"][card]
    
    return initial_count_player

#Draws 1 card for the CPU (Dealer) and adds them to the dictionary. Returns the hand of the CPU
def initial_draw_CPU():
    CPU_C = random.choice(cards)
    initial_count_CPU = 0
    current_game[1]["current_hand"].append(CPU_C)
    initial_count_CPU += current_game[1]["current_hand"][0]
    
    return initial_count_CPU

#Function that adds a card to the hand of the selected player. "name" must be either "Human" or "CPU". It returns the new card of the player
def add_card(name, count):
    new_card = random.choice(cards)
    if new_card == 11 and count > 10:
        new_card == 1
    for i in range(2):
        if current_game[i]["player"] == name:
            current_game[i]["current_hand"].append(new_card)
    return new_card
            


def game():
    #Cleans the dictionaries after a fresh game
    for i in range(2):
        current_game[i]["current_hand"] = []
    
    #Variable that controls the loop of the game
    stop_game = False
    
    while stop_game == False:
        start_game = input("Do you want to play a game of Blackjack? Type 'y' to start or 'n' to stop the code: ").lower()
        if start_game == "n":
            stop_game = True
            return
        
        else:
            player_count = initial_draw_player()
            player_hand = current_game[0]["current_hand"]
            CPU_count = initial_draw_CPU()
            CPU_hand = current_game[1]["current_hand"]
          
            print(f"Your current hand: {player_hand}, for a total score of: {player_count}")
            print(f"Computer's first card is: {CPU_count}\n")
            
            #Check if the player has a 21 in their hand and then calculate CPU's hand
            if player_count == 21:
                print("Blackjack! Calculating house's hand.")
                while CPU_count < 17:
                    CPU_count += add_card(computer, CPU_count)
                print(f"Your current hand: {player_hand}, for a total score of: {player_count}")
                print(f"Computer's final hand: {CPU_hand}, for a total score of: {CPU_count}\n")
                if CPU_count == 21:
                    print("Computer gets blackjack, the house wins.")
                else:
                    print("You win!\n\n")
                    game()
                    
            else:
                another_card = "y"
                while another_card == "y":
                    another_card = input("Do you want another card? Type 'y' to get another one or 'n' to plant: ").lower()
                    if another_card == "y":
                        player_count += add_card(player, player_count)
                        player_hand = current_game[0]["current_hand"]
                        print(f"Your current hand: {player_hand}, for a total score of: {player_count}")
                        print(f"Computer's first card is: {CPU_count}")
                    if player_count > 21:
                        another_card = "n"
                        print(f"Your score is {player_count}. That is over 21! You lose")
                        game()
                
                while CPU_count < 17:
                    CPU_count += add_card(computer, CPU_count)
                print(f"Your final hand is: {player_hand}, for a total score of: {player_count}")
                print(f"Computer's final hand: {CPU_hand}, for a total score of: {CPU_count}\n")
                if CPU_count == 21:
                    print("Computer gets blackjack, the house wins.\n")
                    game()
                elif CPU_count == player_count:
                    print("It's a draw\n")
                    game()
                elif CPU_count > 21:
                    print("Computer went over 21. You win!\n")
                    game()
                elif player_count > CPU_count:
                    print(f"Player wins with a score of {player_count}")
                    game()
                elif player_count < CPU_count:
                    print(f"Computer wins with a score of {CPU_count}")

game()
                
                    
            
          
            
          
            
          
            
          
            