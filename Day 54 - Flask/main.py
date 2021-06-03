cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 54 -
"""
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.env")
FLASK_APP = os.getenv("FLASK_APP")
app = Flask(__name__)

def make_biu(fnc):
    def wrapper():
        return f"<h1><em><b><u>{fnc()}</u></b></em></h1>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 class="title"> Hello, World!</h1>'

@app.route('/bye')
@make_biu
def bye():
    return "Ha, leaving?"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Heyo {name}, you have {number} to live!"
    
    
# Executing the code withing the file. This should always be the last
if __name__ == '__main__':
    app.run()

