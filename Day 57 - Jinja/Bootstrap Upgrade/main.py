cls = lambda: print("\033[2J\033[;H", end='')
cls()

from flask import Flask, render_template, request
import requests
import post


app = Flask(__name__)
post_list = []
blog_entries = requests.get(url="https://api.npoint.io/43644ec4f0013682fc0d").json()
post_list = []   

for entry in blog_entries:
    title = entry["title"]
    subtitle = entry["subtitle"]
    body = entry["body"]
    post_id = entry["id"]
    
    new_post = post.Post(post_id=post_id, post_body=body, post_subtitle=subtitle, post_title=title)
    post_list.append(new_post)
        
@app.route('/')
def home():          
    return render_template("index.html", entries = post_list)

@app.route('/blog/<post_id>')
def entry(post_id):
    return render_template("post.html", post_id=post_id, entry=post_list[int(post_id)-1])

@app.route('/<page_name>')
def load_page(page_name):
    if page_name == "index":   
        return render_template(f"{page_name}.html", entries=post_list)
    elif page_name == "contact":
        pass
    else:
        return render_template(f"{page_name}.html")

@app.route('/prototype')
def proto_page():
    return render_template("contactindex.html")

# Creating a decorator to catch form POST requests
@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        name = request.form["username"]
        email =  request.form["user-mail"]
        cel = request.form["user-phone"]
        message = request.form["user-message"]
        print(f"{name}\n{email}\n{cel}\n{message}")
        return render_template("contact.html", header_message="Your message was received succesfully", subheader="We will get in contact with you.")
    else:
        return render_template("contact.html", header_message="Contact Me", subheader="Have questions? I have answers.")

if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
