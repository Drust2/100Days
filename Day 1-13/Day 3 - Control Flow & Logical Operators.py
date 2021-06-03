import random
# -*- coding: utf-8 -*-
cls = lambda: print("\033[2J\033[;H", end='')
cls()

randomnum = random.randint(10, 99)
randomnumS = str(randomnum)

"""
Conditional Statements:
    if - elif - else

    If we want, for example, to fill a bathtub:
        water_lever = 50
        if water_level > 80:
            print("Drain Water")
        else:
                print("Continue")
    
Logical Operators:
    < :  Less than
    > :  Greater than
    >= : Greater or equal than
    <= : Less or equal than
    == : Equal to
    != : Not Equal to
    and
    or
    not : a = 15: a > 16 = false; not a > 16 = True (Reverses condition)
    
Code Blocks:
    
Scope:
    
    
    
str.lower() = Lowercases all the characters in the string
str.count(str2) = Counts the amount of the selected character in the string
"""
print("Interactive task #1:\n")
# Modulo (%) gives you the remainder of a number after a division. e.g. 
# 4%2 = 0; 5%2 = 1 (5/2 = 2*2+1); 14%4 = 2 (14/4 = 4*3+2)

P1InputS = randomnumS
print(f"{P1InputS} is your number")
Remainder = int(P1InputS)%2
if Remainder == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
print("\nInteractive task #2:\n")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/(height**2), 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")
    
print("\nInteractive task #3:\n") 

# 🚨 Don't change the code below 👇
InputYear = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
EvenDivby4 = (InputYear%4)
EvenDivby100 = (InputYear%100)
EvenDivby400 = (InputYear%400)
StrLeap = "Leap Year."
StrNotLeap = "Not leap year."

if EvenDivby4 == 0:
    if EvenDivby100 == 0:
        if EvenDivby400 == 0:
            print(StrLeap)
        else:
            print(StrNotLeap)
    else:
        print(StrLeap)
else:
    print(StrNotLeap)
    
print("\nInteractive task #4:\n") 

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
SPizza = 15
MPizza = 20
LPizza = 25
SPep = 2
MLPep = 3
ECheese = 1
Bill = 0

if size == "S":
    Bill = SPizza
    if add_pepperoni == "Y":
        Bill += SPep
    if extra_cheese == "Y":
        Bill += ECheese
elif size == "M":
    Bill = MPizza
    if add_pepperoni == "Y":
        Bill += MLPep
    if extra_cheese == "Y":
        Bill += ECheese
elif size == "L":
    Bill = LPizza
    if add_pepperoni == "Y":
        Bill += MLPep
    if extra_cheese == "Y":
        Bill += ECheese
else:
    print("We serve food here sir.\n")
    print("""    
//////////////////////////////////////////////////
////+////////////////////////////+oyhs////////////
//////////////////////////////oo+/::yso///////////
+///////////////////////////+s/--.--o+oo//////////
///////////////////////////oo:-....-o//y++++++++++
//////////////////////////os//-...-:s:os++++++++++
//////////////////////++/+s/+:-...-o//y+++++++++++
///////////////////////++y++/---.-/o:os++++oo+++++
/////////////////////+++os:+------s//yo+++++++++++
///////////+//++++++++++y//:-...-++:so++++++++++++
////////+++++++++++++++os:/:-..-:s/os+++++++++++++
//////+++++++++++++++++s//+:----o+/y++++++++++++++
//+++++++++++++++++++++y---...-:s/so++++//+++/////
++++++++++++++++++++++os-------o++y++/////////////
+++++++++++++osysssssoso:////::s/so///////////++++
+++++++++///+hhdddddhyyhmmNmmmdyos+////////+++++++
++++////////+ddddddddddhhhmNNNNNh+/+++++++++++++++
+///////////+ohddddddhhhdhyydmmmhoo+++++++++++++++
/////////+++ossyso+++//oo++oooso+ooosso+++++++++++
/+//+/++ossso+oo//+//////////+///+////+oss++++++++
++++++oys++o+/////++////////++//////////+oys++++++
+++++yy+///////////////////////////+o///o+/oyo++++
///oho//////////////////////////////////////oh++++
/++ho////+ooo+////////////+oooo+/////////////ho+++
++oh////++//+oo/////////oso+///so////////////hs+++
++sy//////////++///////o+///////////////////+ho+++
++oy///////oooooo+/////+o+os++/////////////+yo++++
+++yo/////so+++++yo//+s+:--/o/////////////syo+++++
++++ys///ss++++++y++sds-----s//////////+sys+++++++
+++++syo+yssyyo++oyoddo-----o+//////+ssso+++++++++
+++++++oyhs+dh:---s/hds-----s+/ssosso+++++++++++++
+++++++++oy/hh::+oy/hdy----:y//y++++++++++++++++++
++++++++++soshyo+/os//:---:s+//y++++++/++++++++/+/
+++++++++++sys+///sso+/:/+o+///y+/+++//////////+++
+++++++++++ss/////y+//+++//////y+/////////////++++
++++++++++oh//////syo+/////////y+/////////////++++
++++++++++ss//////+h++o+/////oossoo/////////////++
+++//////+yo///////shyo//////+o+/+ss/////////+++++
////////+sys////////hddyo//+osoo//oy+//////+++++++
///:////yo+y+///////sdddyooo+++oooo+/+++++++++++++
:://////oooyyo//////ydds//+ssoo+++++++++++++++++++
/////+++++++osso++ohdds/+shs++++++++++++++++++++++
+++++++++++++++hy+oso+/+yoss++++++++++++++++++++++
++++++++++++++++sso+++syd+oy++++++++++++++++++++++
+++++++++++++++++ooooooodo+dhs++++++++++++++++++++
++++////++++++++++++++yhhhohyho++//++//++/////////
+////////////+++/////+dhhdhyyhy////////////+++////
+/++/////////+++/////ydhdhhhhhd+//////////////////
///////////+///////+shhyhyyhhyhy//////////////////
///////////////////odhhyyyydyyyh+/////////////////
//////////////////+hydyyyyydyyyho/////////////////
//////////////////yyhhyyyyydyyyyy/////////////////
//////////////////shdyyyyyyhyyyyd+////////////////
/////////////::::/sydyyyyyydhyhds/////////////////
///////////:::://+hyyyyyyyyho/yhs/////////////////
////////:::://///ysdyyyyyyyd+/hhh/////////////////
/////////////////dsdyyyyyyyh//hhd+////////////////
 """)

print(f"Your final bill is: ${Bill}")

           
 # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Name1 = name1.lower()
Name2 = name2.lower()
Count1 = Name1.count("t") + Name1.count("r") + Name1.count("u") + Name1.count("e") + Name2.count("t") + Name2.count("r") + Name2.count("u") + Name2.count("e")
Count2 = Name1.count("l") + Name1.count("o") + Name1.count("v") + Name1.count("e") + Name2.count("e") + Name2.count("l") + Name2.count("o") + Name2.count("v")
Score = int(str(Count1) + str(Count2))
if Score < 10 or Score > 90:
    print(f"Your score is {Score}, you go together like coke and mentos")
elif Score >= 40 and Score <= 50:
    print(f"Your score is {Score}, you are alright together")
else:
    print(f"Your score is {Score}")
    
    
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
Name = input("First, input your name: ")
print(f"""Your name is {Name}. You are a member of one of the fiercest pirate
      crews that sailed the seven seas... That was, until you were left away
      on this deserted island for drinking all the rum. The situation looks
      dread, there is not a single soul to be seen and the food is scarce.
      Walking for some hours you find some debris. Hoping to find another person
      you actually find a skeleton with a shovel and a piece of paper between
      its hands. The paper results to be a map for the Treasure Island! This
      island is a legend between pirates and sure may be your ticket out of here
      and to a life of pleasure! Your adventure begins here, {Name}\n""")

print("""
 -.,_        .,,,,.        _,.-
  `-_-.,_.,xxx####xxx,._,.-_-'
``"-,"-,\ xx ###### xx /,-",-"''
 `"-=`-,,xx          xx,,-'=-"'
 .,-='`,x,,;,######,;,,x,'`=-,.
'_.-='''x=(O))####((O)=x```=-._`
  .='_.-'x   |####|   x`-._`=.
 ' /'   .-;x |#/\#| x;-.   `\ `
     .-'_.-.x\/  \/x.-._`-.           
    _.='      (CC)      `=._
""")
print("Following the map you arrive to some type of tropical jungle where the path bifurcates between left and right.")
Decision_1 = input("Which path will you take? L or R? ")

if(not Decision_1 == "L" or Decision_1 == "Left" or Decision_1 == "left"):
  print("""As you decide going that way you feel uneasy. The feeling is unbearable, so much that you do not notice the hole and fall into a pit of some sorts. You look everywhere, but escaping does not look like a possibility. GAME OVER\n """)
else:
  print("""
       o                 o
                  o
         o   ______      o
           _/  (   \_
 _       _/  (       \_  O
| \_   _/  (   (    0  \
|== \_/  (   (          |
|=== _ (   (   (        |
|==_/ \_ (   (          |
|_/     \_ (   (    \__/
          \_ (      _/
            |  |___/
           /__/
  """)
  print("""\nIt seems that left was actually the right path. The path was actually a breeze. No danger and straight between the trees. It looks that people actually modified the environment to make some paths. Although, this is not visible from where your trip began. You think to yourself that it is pretty interesting that maps never include instructions on where to go. It seems that whoever makes them just wants to ruin everyone.\n""")

  print("""While pondering about the absurdity of cartography, you arrive to a river full of fish and other animals drinking from the shore. You can't recognize the fish, but some of the animals appear to avoid them.  You devise 2 possibilities. Swimming through the river to the other side and continue your quest, or waiting and rotting in place.\n""")

  Decision_2 = input("What should you do? Swim, Wait or Back? ")
  if Decision_2 == "Swim" or Decision_2 == "swim":
    print("'You are (were) a pirate, what could be so dangerous about river fish?' is what crosses your mind while bravely throwing your body to the river with a big jump fit for someone who walks the plank of a pirate ship. Sadly this decision is rather bad, as the trout-like fishes start biting you everywhere. Those are not very dangerous, but the fear makes you lose momentum and the current of the river drags you. GAME OVER")
  elif Decision_2 == "Wait" or Decision_2 == "wait":
    print("You decide to wait and rot. Probably build a hut or be friends with the animals. As you sit on the ground, the earth starts trembling and a large tree falls from the other side of the river to your side, connecting it so you can pass. Seems you can continue your quest.\n")

    print(""" You finally arrive to a cave. The map instructs you to dig, with the shovel that you thankfully grabbed from the skeleton, in a spot near a tree split nearly in half from a vertical cut just outside the cave. You find the spot and dig until you find a key: \n

    
     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
    \n
    The inscription in the map reads "Choose Wisely". You manage to build a torch with some wood, a cloth and some rum you had on yourself. The walk lasts around 15 minutes until you reach 3 colored doors. Red, blue and yellow. There is no inscription to be found and they can be opened with the key you have. 
    """)
    Decision_3 = input("Which color will you open? Red, Blue or Yellow? ")
    if Decision_3 == 'Red' or Decision_3 == 'red' or Decision_3 == 'R' or Decision_3 == 'r':
      print("""\nAs you open the red door, flames erupt from everywhere, not kidding, even from the floor. GAME OVER. 

                                  (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
         )            . `--=.._____..=--'. ./ 
      """)
    elif Decision_3 == 'Blue' or Decision_3 == 'blue' or Decision_3 == 'B' or Decision_3 == 'b': 
      print("""\nAs you open the blue door, you are instantly mawled by some wretched looking beasts. It seems there is no escape now. GAME OVER

             ___
          .="   "=._.---.
        ."         c ' Y'`p
       /   ,       `.  w_/
       |   '-.   /     / 
 _,..._|      )_-\ \_=.\
`-....-'`------)))`=-'"`'"
      """)
    elif Decision_3 == 'Yellow' or Decision_3 == 'yellow' or Decision_3 == 'y' or Decision_3 =='Y':
      print(f"""\nCongratulations! You have opened the door and reached the treasure. Here you find all sorts of coins, jewels, armor, weapons and even a boat for you to return home. The legend of {Name} will be remembered forever. \n
      """)
      print("""
                                                                     .
                                     .
          ,d88b,                                     .                   __..-
          888888                                        .            .--SEAL:.
          `?88P'         .                       __                ,'WWII::.
                                               .MW:`-.            /WWII::..
                                       .    _.MWII:'. `.     .  ,'WII::..
                                        _.-MWII::'.     `-.   ,'WWI::.
    .                          _..vvvv,'WWII::'            `.'WII::.
                            ,-'WI:'''/WII:'.                 \WI:.
--------------------.==.--,'WWI:'.  /WI:'.          :.        `.I:.
            -.      (88),'WWI:'.  ,'I:.              ::.        \..
     -    ~-~_~ _./d88P/\?I:'.   /WI:.                ::.        \ .
          ~-~-,-~' ~~~ / )------'WI:.____ _.d88P_____::::.        \
   _       ,-'  .     /
      """)
    
    else:
      print(f"\nAs you try, a boulder traps the cave and blocks your exit. Between the chaos, the flame of your torch goes out and you lose it. It appears to be the end of {Name}. GAME OVER")

  else:
    print("\nFilled by cowardice you try your plan but fails miserably, as there is an earthquake that suddenly ruins all your possibilities. Your lack of decision is going to be recorded forever in history. That is, if someone finds this island again. GAME OVER")
           
          