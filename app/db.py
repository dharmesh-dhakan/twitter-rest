# !/usr/bin/env python3
from flask import Flask
from config import configDict
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{configDict["db_user"]}:{configDict["db_password"]}@localhost:3306/{configDict["db_name"]}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.user import User

db.create_all()
db.session.commit()