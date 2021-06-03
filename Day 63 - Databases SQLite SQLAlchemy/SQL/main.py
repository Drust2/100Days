cls = lambda: print("\033[2J\033[;H", end='')
cls()



# # Creating a SQL table the RAW way
# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter: The Prisoner of Azkaban', 'J.K. Rowling', '9.2')")
# db.commit()

# Creating a SQL Table with SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    
    def __repr__(self):
        dictionary = {
                "title": self.title,
                "author": self.author,
                "rating": self.rating,
            }
        return '<%r>' % dictionary

# # Creating a new table
# db.create_all()

# # Creating a new record
# book_1 = Book(id = 1, title = 'Harry Potter: The Prisoner of Azkaban', author = 'J.K. Rowling', rating = 9.2)
# db.session.add(book_1)
# db.session.commit()

# # Reading all records
# all_books = db.session.query(Book).all()

# # Reading a particular entry by query
# book = Book.query.filter_by(title="Harry Potter").first()

# # Update a record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# # Update a record by PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()  

# # Delete a record by PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


