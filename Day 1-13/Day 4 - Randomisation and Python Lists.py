import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = round(random.random()*100, 2)
randomnumS = str(randomnum)

'''
Randomisation and Python Lists+

Lists:
    Ways to group variables. The order depends on the order of the things are
    written. Lists naturally can use subscripts.
    fruits = ["Cherry", "Apple", "Pear"]
    print(fruits[0]) = Cherry
    
    list.append(x) = Adds x at the end of the list
    list.insert(i,x) = Inserts item x in position i
    list.remove(x) = Removes the first item of value x
    list.pop([i]) = Removes the item at index i and returns it. It removes and 
                    returns the last item if no i is specified.
    list.clear() = Removes all items from the list
    list.index(x[, start[, end]]) = Returns first item whose value is x. 
                                    start and end limits the range of search.
    list.count(x) = Counts how many x items there are on the list
    list.reverse() = Reverse the elements of the list in place
    list.copy() = Returns a copy of the list.
    
    random.choice(list) = Chooses a random object from a selected list
    random.shuffle(list) = Shuffles the elements of a container
    
Nested list: A list that contains other lists:
    fruits = ["Apples", "Nectarines", "Tomatoes"]
    vegetables = ["Potato", "Kale", "Spinach"]
    fruits_vegetables = [fruits, vegetables]

'''

# Interactive Project #1
#Remember to use the random module 👇


# 🚨 Don't change the code below 👇
test_seed = randomnum
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
HeadTails = random.randint(0, 1)
if HeadTails == 1:
    print("Heads")
else:
    print("Tails")
    
    
# Interactive Project #2

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
List_Length = len(names)
Random_num = random.randint(1, List_Length)
Randu = Random_num-1
Pays = names[Randu]
print(f"{Pays} is going to buy the meal today!")


# Interactive Project #3
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position_1 = int(position[0])-1
position_2 = int(position[1])-1
map[position_1][position_2] = "X"
#position.insert([position_1][position_2], "X")





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Project #4
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Possibility = [rock, paper, scissors]
Human_Selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
COM_Selection = random.randint(0,2)
Player = Possibility[Human_Selection]
COM = Possibility[COM_Selection]

print(Player + "\n")
print("Computer chose:\n")
print(COM + "\n")

if Human_Selection == 0 and COM_Selection == 0:
  print("It's a draw.")
elif Human_Selection == 0 and COM_Selection == 2:
  print("You win.")
elif Human_Selection == 0 and COM_Selection == 1:
  print("You lose.")
elif Human_Selection == 1 and COM_Selection == 0:
  print("You win.")
elif Human_Selection == 1 and COM_Selection == 2:
  print("You lose.")
elif Human_Selection == 1 and COM_Selection == 1:
  print("It's a draw.")
elif Human_Selection == 2 and COM_Selection == 0:
  print("You lose.")
elif Human_Selection == 2 and COM_Selection == 2:
  print("It's a draw.")
elif Human_Selection == 2 and COM_Selection == 1:
  print("You win.")

