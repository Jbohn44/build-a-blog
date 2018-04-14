from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1240))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['GET', 'POST'])
def index():

    blogs = Blog.query.all()
    return render_template('index.html', blogs = blogs)

@app.route('/newpost', methods=['GET', 'POST'])
def new_post():
    
    if request.method == 'POST':
        blog_title = request.form['title']
        blog_body = request.form['blog-body']
        new_post = Blog(blog_title, blog_body)
        db.session.add(new_post)
        db.session.commit()

    return render_template('newpost.html')
@app.route('/postpage', methods=['GET', 'POST'])
def blog_post_page():
    return render_template('posted.html')


if __name__ == '__main__':
    app.run()