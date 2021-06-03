cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day X -
"""
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.env")
FLASK_APP = os.getenv("FLASK_APP")


