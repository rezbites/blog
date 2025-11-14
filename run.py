from main import app


#can avoid using the if __name__ == "__main__": block in production
#but it's a good practice to include it for clarity and to prevent code from running when imported
#use flask --app main --debug run directly in terminal to run the app
if __name__ == "__main__":  
    app.run(debug = True)