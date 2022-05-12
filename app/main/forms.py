from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    '''
    UpdateProfile class to create instances of updateprofile objects
    '''
    bio = TextAreaField('Tell us a little about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class UploadPitch(FlaskForm):
    '''
    
    '''
    message = TextAreaField('Write your pitch', validators= [InputRequired()])
    author = TextAreaField('Name of author', validators = [InputRequired()])
    category = SelectField('Category', choices=(['Food', 'Sports', 'Travel', 'Art', 'Music', 'Film', 'Lifestyle', 'Other']), validators = [InputRequired()])
    submit = SubmitField('Post')