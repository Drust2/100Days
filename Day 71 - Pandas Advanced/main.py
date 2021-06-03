cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 71 - Pandas data exploration
"""
import pandas as pd

df = pd.read_csv("salaries_by_college_mayor.csv")


