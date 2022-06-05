from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

#app = Flask(__name__)
app = Flask(__name__)

# app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentimentDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# for migrating db (synching model into db):
migrate = Migrate(app, db)
# terminal:
# pip install flask-migrate
# flask db init //makes a directory for migration
# flask db stamp head
# flask db migrate
# flask db upgrade

# Setting the upload folder
UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from routes import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)


