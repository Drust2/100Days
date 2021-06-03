cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 54 - Higher Lower
"""
import server
import random

answer_number = random.randint(1, 10)
flask_server = server.Server(answer_number)
app = flask_server.app

lower_list = []
higher_list = []

for i in range(9):
    if i < answer_number:
        lower_list.append(i)
    if i > answer_number:
        higher_list.append(i)
        
@app.route("/")
def home():
    return "<h1> Higher Lower Game </h1>\n<hr>\n<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>\n <p> Try guessing a number in the URL between 1 and 9."

   
@app.route('/<int:appitemid>')
def check(appitemid):
    if appitemid < answer_number:
        return "<h1> Lower </h1>\n<hr>\n<p>You should try to aim a little higher here</p>"
    elif appitemid > answer_number:
        return "<h1> Higher </h1>\n<hr>\n<p>You should try to aim a little lower here</p>"
    else:
        return "<h1> Good Job! </h1>"        

flask_server.run()