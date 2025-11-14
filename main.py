from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm




app = Flask(__name__)


app.config['SECRET_KEY'] = 'df20cd524044f455dc80007d4bb3f328'




<<<<<<< HEAD
posts = [ 
=======
posts = [
>>>>>>> d610aee1a2440cf2685d8c62ec8e2cc4ee1497cd
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

<<<<<<< HEAD
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' Accont created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='registration', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='login', form=form)
=======

@app.route('/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Acoount created {form.username.data}!', 'success')
        redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)
>>>>>>> d610aee1a2440cf2685d8c62ec8e2cc4ee1497cd


#can avoid using the if __name__ == "__main__": block in production
#but it's a good practice to include it for clarity and to prevent code from running when imported
#use flask --app main --debug run directly in terminal to run the app
if __name__ == "__main__":  
    app.run(debug = True)