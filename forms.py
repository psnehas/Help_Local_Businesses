from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, TextField, SubmitField,PasswordField,SelectField,DateField
from wtforms.validators import (DataRequired, Length,Email,EqualTo,URL)

class RegisterBookseller(FlaskForm):
    """Bookseller Contact form."""
    storeName = StringField('Name of the Store', [DataRequired()])
    storeLocation = StringField('Location',[DataRequired()])
    storeOwnerName = StringField('Name of the owner',[DataRequired()])
    storeContactNum = StringField('Owner Contact Number',[DataRequired()])
    storeOwnerEmail = StringField('Email address', [Email(message=('Not a valid email address.')),DataRequired()])
    StoreOwnerPassword = StringField('Password',[DataRequired()])

class RegisterCustomer(FlaskForm):
    """Customer contact form"""
    firstName = StringField('First Name', [DataRequired()])
    lastName = StringField('Last Name',[DataRequired()])
    customerEmail = StringField('Email', [Email(message=('Not a valid email address.')),DataRequired()])
    customerPassword = StringField('Password',[DataRequired()])
    customerZipCode = StringField('ZipCode',[DataRequired()])
    

class CustomerSearchBar(FlaskForm):
    """Customer search queries"""
    pass

class LoginSeller(FlaskForm):
    emailAddress = StringField("Email", [DataRequired()])
    password = StringField("Password",[DataRequired()])
    


