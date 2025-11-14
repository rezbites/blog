from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo 

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()  ])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up') 

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators = [DataRequired(), Email()  ])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login Up') 
=======

from wtforms import StringField, PasswordField, SubmitField, BooleanField #these are the fields we want to use in our form
from wtforms.validators import DataRequired, Length, Email, EqualTo #these are the validators we want to use in our form 


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  
    email = StringField('Email', validators =[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  
    email = StringField('Email', validators =[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  #optional field for remember me functionality
    submit = SubmitField('Login')
    
>>>>>>> d610aee1a2440cf2685d8c62ec8e2cc4ee1497cd
