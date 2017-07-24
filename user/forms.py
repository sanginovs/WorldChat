from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError  #this is one of the features of WTForms; allows custom validators database level checking



#separate import of python packages(above) and application level packages

from user.models import User


class RegisterForm(Form):
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])
    email = EmailField('Email address', [
        validators.DataRequired(),
        validators.Email()
        ]
    )
    username = StringField('Username', [
        validators.DataRequired(),
        validators.length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords should match'),
        validators.length(min=4, max=80)
        ])
    confirm = PasswordField('Confitm Password')
    
    
    def validate_username(form, field):
        '''this function will check for username in database to prevent dupplication'''
        if User.objects.filter(username=field.data).first():
            raise ValidationError("Username already exists")
            
    def validate_email(form, field):
        '''this function will check for email in database to prevent dupplication'''
        if User.objects.filter(email=field.data).first():
            raise ValidationError("Email is already in use")


class LoginForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.length(min=4, max=25)
        ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=4, max=80)
        ])
    #submit=SubmitField("Sign in")
    
    
    
        
