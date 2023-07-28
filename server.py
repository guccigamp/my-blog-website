from flask import Flask, request
from flask import render_template
import requests

all_blogs = requests.get(url="https://api.npoint.io/476c0ef2dcf7814c9f99").json()

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html', all_blogs=all_blogs["blogs"])

@app.route('/blogs')
def blogs():
    return render_template('blogs.html', all_blogs=all_blogs["blogs"])

@app.route('/blogs/<sn>/<blog>')
def blog_post(sn, blog:str):
    blog = eval(blog)
    return render_template('single-post.html', sn=sn ,blog=blog)

@app.route('/about-me')
def about():
    return render_template('about.html')

@app.route('/contact-me')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)