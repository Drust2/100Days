from flask import Flask, render_template
import requests
import post


app = Flask(__name__)
post_list = []
@app.route('/')
def home():
    global post_list
    blog_entries = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()
    post_list = []   
    
    for entry in blog_entries:
        title = entry["title"]
        subtitle = entry["subtitle"]
        body = entry["body"]
        post_id = entry["id"]
        
        new_post = post.Post(post_id=post_id, post_body=body, post_subtitle=subtitle, post_title=title)
        post_list.append(new_post)
        
       
    return render_template("index.html", posts = post_list)

@app.route('/post/<post_id>')
def entry(post_id):
    return render_template("post.html", post_id=post_id, entry=post_list[int(post_id)-1])

if __name__ == "__main__":
    app.run(debug=True)
