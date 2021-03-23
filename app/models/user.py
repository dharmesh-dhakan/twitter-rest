#!/usr/bin/env python3
from flask import Flask, jsonify, request
from db import db


class User(db.Model):
    ''' The data model'''
    # table name
    __tablename__ = 'users'
    __table_args__ = (
        db.UniqueConstraint('email'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}