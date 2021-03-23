#!/usr/bin/env python3
from flask import jsonify, request
from flask_restful import Resource
import services.user_service as user_service
from models.user import User
import json


class UserResource(Resource):
    def get(self):
        users = user_service.get()
        return jsonify([user.as_dict() for user in users])

    def post(self):
        user = user_service.create(request.json)
        return jsonify(user.as_dict())