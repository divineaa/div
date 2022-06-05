
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired,Email,EqualTo, Length
from flask_wtf.file import FileField

class AddArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Title', validators=[DataRequired()])
    location = SelectField(u'Location', choices=[('0', 'Select Location'),('Abra', 'Abra'), ('Agusan del Norte', 'Agusan del Norte'), ('Agusan del Sur', 'Agusan del Sur'), ('Aklan', 'Aklan'), ('Albay', 'Albay'), ('Antique', 'Antique'), ('Apayao', 'Apayao'), ('Aurora', 'Aurora'), ('Baguio City', 'Baguio City'), ('Basilan', 'Basilan'), ('Bataan', 'Bataan'), ('Batanes', 'Batanes'), ('Batangas', 'Batangas'), ('Benguet', 'Benguet'), ('Biliran', 'Biliran'), ('Bohol', 'Bohol'), ('Bukidnon', 'Bukidnon'), ('Bulacan', 'Bulacan'), ('Cagayan', 'Cagayan'), ('Camarines Norte', 'Camarines Norte'), ('Camarines Sur', 'Camarines Sur'), ('Camiguin', 'Camiguin'), ('Capiz', 'Capiz'), ('Catanduanes', 'Catanduanes'), ('Cavite', 'Cavite'), ('Cebu', 'Cebu'), ('Cotabato', 'Cotabato'), ('Davao de Oro (Compostela Valley)', 'Davao de Oro (Compostela Valley)'), ('Davao del Norte', 'Davao del Norte'), ('Davao del Sur', 'Davao del Sur'), ('Davao Occidental', 'Davao Occidental'), ('Davao Oriental', 'Davao Oriental'), ('Dinagat Islands', 'Dinagat Islands'), ('Eastern Samar', 'Eastern Samar'), ('Guimaras', 'Guimaras'), ('Ifugao', 'Ifugao'), ('Ilocos Norte', 'Ilocos Norte'), ('Ilocos Sur', 'Ilocos Sur'), ('Iloilo', 'Iloilo'), ('Isabela', 'Isabela'), ('Kalinga', 'Kalinga'), ('La Union', 'La Union'), ('Laguna', 'Laguna'), ('Lanao del Norte', 'Lanao del Norte'), ('Lanao del Sur', 'Lanao del Sur'), ('Leyte', 'Leyte'), ('Maguindanao', 'Maguindanao'), ('Marinduque', 'Marinduque'), ('Masbate', 'Masbate'), ('Misamis Occidental', 'Misamis Occidental'), ('Misamis Oriental', 'Misamis Oriental'), ('Mountain Province', 'Mountain Province'), ('Negros Occidental', 'Negros Occidental'), ('Negros Oriental', 'Negros Oriental'), ('Northern Samar', 'Northern Samar'), ('Nueva Ecija', 'Nueva Ecija'), ('Nueva Vizcaya', 'Nueva Vizcaya'), ('Occidental Mindoro', 'Occidental Mindoro'), ('Oriental Mindoro', 'Oriental Mindoro'), ('Palawan', 'Palawan'), ('Pampanga', 'Pampanga'), ('Pangasinan', 'Pangasinan'), ('Quezon', 'Quezon'), ('Quirino', 'Quirino'), ('Rizal', 'Rizal'), ('Romblon', 'Romblon'), ('Samar', 'Samar'), ('Sarangani', 'Sarangani'), ('Siquijor', 'Siquijor'), ('Sorsogon', 'Sorsogon'), ('South Cotabato', 'South Cotabato'), ('Southern Leyte', 'Southern Leyte'), ('Sultan Kudarat', 'Sultan Kudarat'), ('Sulu', 'Sulu'), ('Surigao del Norte', 'Surigao del Norte'), ('Surigao del Sur', 'Surigao del Sur'), ('Tarlac', 'Tarlac'), ('Tawi-Tawi', 'Tawi-Tawi'), ('Zambales', 'Zambales'), ('Zamboanga del Norte', 'Zamboanga del Norte'), ('Zamboanga del Sur', 'Zamboanga del Sur'), ('Zamboanga Sibugay', 'Zamboanga Sibugay')])
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

    