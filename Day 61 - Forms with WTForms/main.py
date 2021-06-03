from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.secret_key = "YaLiTSuP4H4x0R"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # VVvalidating that the page is receiving a POST request
    if login_form.validate_on_submit():
        email_data = login_form.email.data
        password_data = login_form.password.data
        if email_data == "admin@email.com" and password_data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()