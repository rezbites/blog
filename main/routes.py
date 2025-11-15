from flask import render_template, flash, redirect, url_for
from main import app, db, bcrypt
from main.models import User, Post
from main.forms import RegistrationForm, LoginForm


posts = [ 
{
    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'This is the content of the first blog post.',
    'date_posted': 'April 20, 2023'
},

{
    'author': 'Jane Smith',
    'title': 'Blog Post 2',
    'content': 'This is the content of the second blog post.',
    'date_posted': 'April 21, 2023'
}

]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash('form.password.data').decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, now you can log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='registration', form=form)




@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)


