cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 24 - Files, Directories, Paths

"""
with open("Day24_Dummyfile.txt", "r") as file:
    lines = file.read()
