cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 54 - server
"""
from dotenv import load_dotenv
from flask import Flask
from flask_classful import FlaskView, route
import os

load_dotenv(dotenv_path="config.env")
FLASK_APP = os.getenv("FLASK_APP")

class Server:
    def __init__(self, answer):
        self.app = Flask(__name__)
        self.number = answer
    
    def run(self):
        self.app.run()
        
        

    

