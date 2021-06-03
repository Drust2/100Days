from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import NumberRange, InputRequired
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
load_dotenv(dotenv_path="config.env")
TMDB_API = os.getenv("TMDB_API")
api_url_search = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API}"
api_url_getmovie = f"https://api.themoviedb.org/3/movie/"
api_url_image = f"http://image.tmdb.org/t/p/w342"

class AddForm(FlaskForm):
    movie_name = StringField('Write the name of a movie', validators=[InputRequired()])
    submit = SubmitField()
    
# Defining the class for the edit form
class EditForm(FlaskForm):
    rating = FloatField('Place a new rating between 0.0 and 10.0:', validators=[InputRequired(), NumberRange(min=0, max=10)])
    review = StringField('Write a new review:', validators=[InputRequired()])
    submit = SubmitField()
    
# Defining the class for each movie object
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer, nullable=False, unique=False)
    review = db.Column(db.String)
    img_url = db.Column(db.String, nullable=False)
    
# Creating the database
db.create_all()

# # Adding a test object
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

database_data = []
@app.route("/")
def home():
    global database_data
    database_data = Movie.query.order_by(Movie.rating).all()
    
    for i in range(len(database_data)):
        database_data[i].ranking = len(database_data)-i
    db.session.commit()
    return render_template("index.html", movies = database_data)

@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    current = Movie.query.filter_by(id=movie_id).first()
    editform = EditForm()
    if editform.validate_on_submit():      
        current.rating = editform.rating.data
        current.review = editform.review.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit.html", movie=current, form=editform)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    current = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(current)
    db.session.commit()
    return redirect("/")

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        search_movie = form.movie_name.data
        return redirect(f"/search/{search_movie}")
    else:
        return render_template("add.html", form=form)
    
@app.route("/search/<movie_name>")
def search(movie_name):
    response = requests.get(url=api_url_search, params={"query": movie_name,}).json()["results"]
    return render_template("select.html", movie_list = response)   

@app.route("/selection/<int:movie_id>")
def selection(movie_id):
    movie_request = requests.get(url=f"{api_url_getmovie}{movie_id}", params={"api_key":TMDB_API, "language": "en-US"}).json()
    new_movie = Movie(
        title = movie_request["title"],
        year = movie_request["release_date"].split("-")[0],
        description = movie_request["overview"],
        rating = 0,
        ranking = len(db.session.query(Movie).all()) + 1,
        review = "None",
        img_url = requests.get(url=f"{api_url_image}{movie_request['poster_path']}").url,
        )
    db.session.add(new_movie)
    db.session.commit()
    databased_movie = Movie.query.filter_by(title=movie_request["title"]).first()
    return redirect(f"/edit/{databased_movie.id}")
    
# Program execution 
if __name__ == '__main__':
    app.run(debug=True)
    # app.run()


    
