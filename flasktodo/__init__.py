import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '05c9681678fa66c1ccbbe721caedcc8b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)

from flasktodo import routes
