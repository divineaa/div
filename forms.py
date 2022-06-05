
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired,Email,EqualTo, Length
from flask_wtf.file import FileField

class AddArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Title', validators=[DataRequired()])
    location = SelectField(u'Location', choices=[('0', 'Select Location'),('Atok', 'Atok'), ('Baguio', 'Baguio'), ('text', 'Plain Text')])
    # file upload/picture
    article_pic = FileField("Article Picture")
    submit = SubmitField('Post Article')

class AddCommentForm(FlaskForm):
    description = TextAreaField('Title', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Post Comment')

class DeleteArticleForm(FlaskForm):
    submit = SubmitField('Delete')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators =[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password1')])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    mname = StringField('Middle Name')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    