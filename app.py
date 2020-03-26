from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import registrationform, loginform
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'eae9943fd8301935b10cde108eb0b2b1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model): #table_name = user
    id = db.Column(db.Integer, primary_key=True) #automatic id generation
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) #rel between two tables, is not an attribute but a function to get all posts from the Post table

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model): #table_name = post
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


#these are the individual blog posts. think of it as a database call, that returns this dict and saved in posts:list of dicts
posts_db = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts_db)


@app.route("/about")
def about():
	return render_template('about.html',title = 'About Page')


@app.route("/register", methods=['POST', 'GET'])
def register():
    form_filled_register = registrationform()
    if form_filled_register.validate_on_submit():
        flash(f'Account created for {form_filled_register.uname.data}!', 'success')
        return redirect(url_for('home')) #name of funtion to that route
    return render_template('register.html',title = 'Register', form = form_filled_register)


@app.route("/login",  methods=['POST', 'GET'])
def login():
    form_filled_login = loginform()
    if form_filled_login.validate_on_submit():
        if form_filled_login.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',title = 'LogIn', form = form_filled_login)


if __name__ == "__main__":
	app.run(debug=True)
