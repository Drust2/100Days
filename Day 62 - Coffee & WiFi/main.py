from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_rating = ["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️" ]
wifi_rating = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪" ]
power_rating = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌🔌" ]

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Quality', choices = coffee_rating ,validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Quality', choices = wifi_rating, validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Availability', choices = power_rating, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(r'./cafe-data.csv', mode="a", newline='', encoding="utf8") as csv_file:
            append_string = f"\n{form.cafe.data},{form.location_url.data},{form.open_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}"
            csv_file.write(append_string)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(r'./cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
