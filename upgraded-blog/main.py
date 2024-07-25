from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
    response = requests.get(blog_url)
    all_blog = response.json()
    return render_template("index.html", all_posts=all_blog)  # Pass data as 'all_posts'

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:num>')
def post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("post.html", post=all_post[num-1])  # Access a single post by index

if __name__ == "__main__":
    app.run(debug=True)
