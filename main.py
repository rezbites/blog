from flask import Flask, render_template

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')







#can avoid using the if __name__ == "__main__": block in production
#but it's a good practice to include it for clarity and to prevent code from running when imported
#use flask --app main --debug run directly in terminal to run the app
if __name__ == "__main__":  
    app.run(debug = True)