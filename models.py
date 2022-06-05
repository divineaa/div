import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
datenow = datetime.datetime.now()


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique = True, index = True)
    password_hash = db.Column(db.String(150))
    firstname = db.Column(db.String(50),nullable=False)
    lastname = db.Column(db.String(50),nullable=False)
    middlename = db.Column(db.String(50),nullable=True)
    joined_at = db.Column(db.DateTime(), default = datenow, index = True)
    articles = db.relationship('Article', backref='user',
                                lazy='dynamic')
    comments = db.relationship('Comment', backref='user',
                                lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Article(db.Model):
    __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}

    id=db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(32),nullable=False)
    article_pic = db.Column(db.String(32),nullable=True)
    location = db.Column(db.String(50),nullable=False)
    date = db.Column(db.DateTime(), default = datenow, index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='article',
                                lazy='dynamic')
    def __repr__(self):
        return f'{self.title} created on {self.date}'

class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}

    id=db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(50),nullable=False)
    date = db.Column(db.DateTime(), default = datenow, index = True)
    location = db.Column(db.String(50),nullable=False)
    sentiment_analysis = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __repr__(self):
        return f'{self.title} created on {self.date}'

db.create_all()
"""
https://stackoverflow.com/questions/37908767/table-roles-users-is-already-defined-for-this-metadata-instance
#creates the db
db.create_all()
#inspects the created tables
from sqlalchemy import create_engine
from sqlalchemy import inspect
engine = create_engine('sqlite:///sentimentDB.db')
insp = inspect(engine)
print(insp.get_table_names())
"""

"""
on the terminal type python3 to enter pthon codes:
->python3
import db:
->from app import db
or
->from models import db
if no module found install:
conda install flask-sqlalchemy
->db.create_all()
add rows:
->from models import Model1, Model2, ModelN
->from datetime import datatime
->t=Task(title="xyz", date=datetime.utcnow())
->db.session.add(t)
->db.session.commit()

issue:
db.session.rollback()


import datetime
d = datetime.datetime.now()

"""