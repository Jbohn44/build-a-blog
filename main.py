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
        title_error = ''
        body_error = ''

        if (blog_title.strip() == ''):
            title_error = "Please enter a title"

        else:
            if (blog_body.strip() == ''):
                body_error = "Please enter a blog"
            
        
    
        if not title_error and not body_error:
            #blog_title = request.form['title']
            #blog_body = request.form['blog-body']
            new_post = Blog(blog_title, blog_body)
            db.session.add(new_post)
            db.session.commit()

        
            return redirect('/blog?id=')
        else:
            return render_template('newpost.html', title_error = title_error, body_error = body_error )

    else:
        return render_template('newpost.html')


#@app.route('/posted')
#def blog_post_page():
    
    #blog_id = 1 #request.form.get['blog-id']
    #blog = Blog.query.get(blog_id)
    


    #return render_template('posted.html', blog = blog)


if __name__ == '__main__':
    app.run()