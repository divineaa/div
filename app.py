from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

#app = Flask(__name__)
app = Flask(__name__)

# app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = os.urandom(32)
#local connection:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentimentDB.db'
#deployed connection:
#postgres://mgketrzpcpmrcb:f140d4f52427c2834b51811d4069f79f18dac8d944ef927a8c25d17b0db88d5f@ec2-34-193-110-25.compute-1.amazonaws.com:5432/dejcu8ol4258oh'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mvpxvsndetkxxk:d8d68cb5070fed476af8afaaa7f5ba6737ad65977ede461d21fe2b5e252c406b@ec2-44-206-204-65.compute-1.amazonaws.com:5432/d22hq5umf5fem6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#added to solve an error
app.app_context().push()
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


