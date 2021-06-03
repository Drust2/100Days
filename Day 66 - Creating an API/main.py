from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Error message for a not found cafe
not_found_error = {"error": {"Not Found": "Sorry, we don't have a cafe in that location"}}
not_exist_error = {"error": {"Not Found": "Sorry, we don't have a cafe with that ID"}}
success_message = {"success": "Successfully added the new cafe."}
success_delete_message = {"success": "Successfully deleted the new cafe."}

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def create_dictionary(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

# Creating a route that lets the user to ask for a random cafe
@app.route("/random", methods=['GET'])
def random_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafe = random.choice(all_cafes)
    cafe_dict = cafe.create_dictionary()
    return jsonify(cafe_dict)

@app.route("/all", methods=['GET'])
def all_cafes():
    all_cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in all_cafes:
        cafe_list.append(cafe.create_dictionary())
    return jsonify(cafe_list)

@app.route("/search", methods=['GET'])
def search_cafe():    
    query_location = request.args.get("loc").capitalize()
    search_result = Cafe.query.filter_by(location=query_location).all()
    if len(search_result) == 0:
        return jsonify(not_found_error)
    else:
        cafe_list = []
        for cafe in search_result:
            cafe_list.append(cafe.create_dictionary())
        return jsonify(cafe_list)

@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
            name = request.form.get("name"),
            map_url = request.form.get("map_url"),
            img_url = request.form.get("img_url"),
            location = request.form.get("loc"),
            seats = request.form.get("seats"),
            has_toilet = bool(request.form.get("toilet")),
            has_wifi = bool(request.form.get("wifi")),
            has_sockets = bool(request.form.get("sockets")),
            can_take_calls = bool(request.form.get("calls")),
            coffee_price = request.form.get("coffee_price"),            
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify()

# Creating a patch method to update a coffee price
@app.route("/edit/<int:cafe_id>", methods=["PATCH"])
def patch_price(cafe_id):
    new_price = request.args.get("new_price")
    to_patch = Cafe.query.filter_by(id=cafe_id).first()
    if to_patch:
        to_patch.coffe_price = new_price
        db.session.commit()
        return jsonify(success_message)
    else:
        return jsonify(not_found_error), 404

# Deleting a cafe ID
@app.route("/report-closed/<int:cafe_id>")
def delete_cafe(cafe_id):
    secret_api = "TopSecretAPIKey"
    query_api = request.args.get("api-key")
    to_delete = Cafe.query.filter_by(id=cafe_id).first()
    if to_delete:
        if query_api == secret_api:
            db.session.delete(to_delete)
            db.session.commit()
            return jsonify(success_delete_message)
        else:
            return jsonify({"error": "Sorry, that's not allowed. Check your API key"}, 403)
    else:
        return jsonify(not_exist_error), 404

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
