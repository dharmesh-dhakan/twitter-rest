#!/usr/bin/env python3
from flask import jsonify, request
from flask_restful import Resource
import services.user_service as user_service
from models.user import User
from flask import abort
import json


class UserResource(Resource):
    def get(self):
        users = user_service.get()
        return jsonify([{"username": user.username} for user in users])

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')

        if username is None or password is None:
            abort(400, {'error_message': 'Username and password is required'})
        if User.query.filter_by(username=username).first() is not None:
            abort(400, {'error_message': 'User already exists'})

        try:
            user = user_service.create(username, password)
        except Exception:
            # add logging for debugging
            abort(500, {'error_message': 'An error has occured'})

        return { 'username': user.username }, 201