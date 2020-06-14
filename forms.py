from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length,Email

class RegisterBookseller(FlaskForm):
    """Contact form."""
    storeName = StringField('Store Name', [DataRequired()])
    storeLocation = StringField('Loacation',[DataRequired()])
    storeOwnerName = StringField('Owner Name',[DataRequired()])
    storecontactNum = StringField('Contact Number',[DataRequired()])
    storeOwnerEmail = StringField('Email', [Email(message=('Not a valid email address.')),DataRequired()])
    # body = TextField('Message', [DataRequired(),Length(min=4, message=('Your message is too short.'))])   ,
    # recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


