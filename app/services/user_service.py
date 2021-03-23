#!/usr/bin/env python
from models.user import User
from db import db
from werkzeug.exceptions import NotFound

def get():
    return User.query.all()

def create(body):
    user = User(**body)
    db.session.add(user)
    db.session.commit()
    return user