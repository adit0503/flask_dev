from flask import Flask, render_template, url_for, flash, redirect
from forms import registration, login
app = Flask(__name__)

app.config['SECRET_KEY'] = 'eae9943fd8301935b10cde108eb0b2b1'

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
    form_filled_register = registration()
    if form_filled_register.validate_on_submit():
        flash(f'Account created for {form_filled_register.uname.data}!', 'success')
        return redirect(url_for('home')) #name of funtion to that route
    return render_template('register.html',title = 'Register', form = form_filled_register)


@app.route("/login")
def login():
    form_filled_login = login()
    return render_template('login.html',title = 'LogIn', form = form_filled_login)


if __name__ == "__main__":
	app.run(debug=True)
