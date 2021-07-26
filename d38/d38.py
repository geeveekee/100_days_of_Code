from re import sub
from flask import Flask, render_template
from post import Post
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    all_post_list = []
    for x in range(4):
        post_x = Post(x)
        all_post_list.append(post_x)
    return render_template("index.html", all_post_list=all_post_list)

@app.route('/dog')
def blog_content():
    title = request.args.get('dog_title')
    subtitle = request.args.get('dog_subtitle')
    body = request.args.get('dog_body')

    
    return render_template("post.html", title=title, subtitle=subtitle, body=body)
