cls = lambda: print("\033[2J\033[;H", end='')
cls()
import random
import pandas
"""
Day 26 - List and Dictionary Comprehension
"""
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
    
# Another way to do it -> List Comprehension
# new_list = [n+1 for n in numbers]

# # Strings
# name = "David"
# letters_list = [i for i in name]

# # Working with range
# doubled_numbers = [n*2 for n in range(1,5)]

# # Conditionals
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [i for i in names if len(i) < 5]
# Long_upper = [i.upper() for i in names if len(i) > 5]

# # Dictionary Comprehension
# # new_dict = {new_key:new_value for item in list}
# # new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# student_score = {i:random.randint(1, 100) for i in names}

# passed_students = {student:score for (student, score) in student_score.items() if score > 70 }

# # Iterating a Pandas dataframe
# people = {
#     "name": ["Caroline", "James", "Lily"],
#     "score": [77, 54, 65],
# }
# dataframe = pandas.DataFrame(people)

# for (index, row) in dataframe.iterrows():
#     # print(row["score"])
#     if row["name"] == "Caroline":
#         print(row["name"])
#         print(row["score"])

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {}
for (index, row) in nato.iterrows():    
    phonetic_dict[row["letter"]] = row["code"]

user_word = input("Type a word: ").upper()
word_letters = [i for i in user_word]
word_list = [phonetic_dict[i] for i in word_letters]
print(word_list)
