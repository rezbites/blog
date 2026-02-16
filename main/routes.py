import os
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from main import app

@app.route('/')
@app.route('/home')
def home():
    posts = []
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    flash("Registration is disabled (Demo Mode - No Database Connected).", "info")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    flash("Login is disabled (Demo Mode - No Database Connected).", "info")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    flash("Logout is disabled (Demo Mode - No Database Connected).", "info")
    return redirect(url_for('home'))

@app.route('/account', methods=['GET', 'POST'])
def account():
    flash("Account page is disabled (Demo Mode - No Database Connected).", "info")
    return redirect(url_for('home'))

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    flash("Post creation is disabled (Demo Mode - No Database Connected).", "info")
    return redirect(url_for('home'))