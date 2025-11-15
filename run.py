from main import app, db
from main.models import User, Post




#doing this to avoid wrapping every time we use shell, so to access db, User, Post directly we can type flask shell instead of python
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


#can avoid using the if __name__ == "__main__": block in production
#but it's a good practice to include it for clarity and to prevent code from running when imported
#use flask --app main --debug run directly in terminal to run the app
if __name__ == "__main__":  
    app.run(debug = True)