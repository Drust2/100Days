cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 56 - main
"""
import server
import requests
from flask import render_template

flask_server = server.Server()
app = flask_server.app



@app.route("/guess/<username>")
def guess_genderage(username):
    name_response = requests.get(url=f"https://api.genderize.io?name={username}").json()
    age_response = requests.get(url=f"https://api.agify.io?name={username}").json()
    name_str = name_response["name"]
    age_int = age_response["age"]
    gen = name_response["gender"]
    probability = name_response["probability"]
    
    return render_template('guess.html', name='guess', user=name_str, age=age_int, gender=gen, prob=probability, copy_year=flask_server.year)

@app.route("/blog/<blog_id>")
def blog_fnc(blog_id):
    data = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()
    return render_template('blog.html', posts=data, copy_year=flask_server.year, blog_id=blog_id)
    
    
flask_server.run()
