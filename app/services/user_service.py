#!/usr/bin/env python3
from models.user import User
from db import db
from werkzeug.exceptions import NotFound

def get():
    return User.query.all()

def create(username, password):
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return user