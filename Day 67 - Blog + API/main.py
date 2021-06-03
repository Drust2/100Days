from flask import Flask, render_template, redirect, url_for, Markup, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditor, CKEditorField
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from sqlalchemy.orm import relationship
from flask_gravatar import Gravatar
import datetime as dt


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

#CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Initializing Gravatar
gravatar = Gravatar(app, 
                    size=150, 
                    rating='g', 
                    default='retro', 
                    force_default=False, 
                    force_lower=False, 
                    use_ssl=False, 
                    base_url=None)

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Admin decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function
        

##CONFIGURE TABLE
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
    
class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.Text, nullable=False)

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# # Creating the databases
# db.create_all()

# Form to register an user
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()]) 
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Register")

# Form to login an user
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", 
                           all_posts=posts, 
                           current_user = current_user, 
                           logged_in = current_user.is_authenticated
                          )


@app.route("/post/<int:index>", methods=['GET', 'POST'])
def show_post(index):
    requested_post = BlogPost.query.get(index)
    comment_form = CommentForm()
    all_comments = Comment.query.filter_by(post_id=requested_post.id).all()
    if comment_form.validate_on_submit():
        commentary = comment_form.comment.data
        new_comment = Comment(
                author_id = current_user.id,
                post_id = requested_post.id,
                text = commentary
            )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(f"/post/{requested_post.id}")
    if requested_post:
        return render_template(
                "post.html", 
                post=requested_post, 
                comment=comment_form, 
                current_user=current_user, 
                logged_in = current_user.is_authenticated, 
                all_comments=all_comments
            )
    else:
        return abort(404)

@app.route("/new-post", methods = ['GET', 'POST'])
@admin_required
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
                title = form.title.data,
                subtitle = form.subtitle.data,
                author_id = current_user.id,
                date = dt.datetime.now().strftime("%B %d, %Y"),
                body = form.body.data,
                img_url = form.img_url.data,
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("make-post.html", form = form, current_user = current_user, logged_in = current_user.is_authenticated)

@app.route("/edit-post/<int:post_id>", methods = ['GET', 'POST'])
@admin_required
def edit_post(post_id):
    actual_post = BlogPost.query.get(post_id)
    form = CreatePostForm()   
    
    if form.validate_on_submit():
        actual_post.title = form.title.data 
        actual_post.subtitle = form.subtitle.data
        actual_post.body = form.body.data
        actual_post.author = form.author.data
        actual_post.img_url = form.img_url.data
        db.session.commit()        
        return redirect(f"/post/{post_id}")
    
    else:
        form.title.data = actual_post.title
        form.subtitle.data = actual_post.subtitle
        form.body.data = actual_post.body
        form.author.data = actual_post.author
        form.img_url.data = actual_post.img_url
        return render_template('make-post.html', form = form, current_user = current_user, logged_in = current_user.is_authenticated)

@app.route("/about")
def about():
    return render_template("about.html", logged_in = current_user.is_authenticated)


@app.route("/contact")
def contact():    
    return render_template("contact.html", logged_in = current_user.is_authenticated)

@app.route("/delete-post/<int:post_id>")
@admin_required
def delete_post(post_id):
    to_delete = BlogPost.query.get(post_id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect("/")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        input_user = form.username.data.lower()
        input_pass = form.password.data
        prompt_user = User.query.filter_by(username=input_user).first()
        
        if not prompt_user:
            flash("This username is not registered")
            return redirect(url_for("login"))
        
        if not check_password_hash(prompt_user.password, input_pass):
            flash("The password is incorrect")
            return redirect(url_for("login"))
        
        else:
            login_user(prompt_user)            
            return redirect("/")
                
    return render_template('login.html', form = form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        input_user = form.username.data.lower()
        input_pass = form.password.data
        input_email = form.email.data
        new_user = User(
                username = input_user,
                password = generate_password_hash(input_pass, method='pbkdf2:sha256', salt_length=8),
                email = input_email
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=form, logged_in = current_user.is_authenticated)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)