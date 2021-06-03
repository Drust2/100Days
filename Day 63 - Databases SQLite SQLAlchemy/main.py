from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False, unique = True)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    
    def __repr__(self):
        dictionary = {
                "title": self.title,
                "author": self.author,
                "rating": self.rating,
            }
        return '<%r>' % dictionary

# Creating the database
db.create_all()

database_data = []

@app.route('/')
def home():
    # Reading all the books from the database and appending them to list
    global database_data
    database_data = db.session.query(Book).all()
    return render_template('index.html', books=database_data)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_title = request.form["title"]
        book_author = request.form["author"]
        book_rating = request.form["rating"]
        
        # Adding the book into the database
        book = Book(title = book_title, author = book_author, rating = book_rating)
        db.session.add(book)
        db.session.commit()
        
    return render_template('add.html')

@app.route("/edit/<book_title>", methods=['GET', 'POST'])
def edit(book_title):     
    if request.method == "POST":
        new_rating = request.form["new_rating"] 
        book_to_update = Book.query.filter_by(title=book_title).first()
        book_to_update.rating = float(new_rating)
        db.session.commit()
        return redirect('/')
    else:
        search = Book.query.filter_by(title=book_title).first()
        return render_template('editrating.html', book=search)     
    
@app.route("/delete/<book_title>")
def delete(book_title):
    book_to_delete = Book.query.filter_by(title=book_title).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')
    

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)


