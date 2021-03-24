# !/usr/bin/env python3
from flask import Flask
from flask_restful import Resource, Api
from db import app
from controllers.user_controller import UserResource


api = Api(app)
api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    ''' run application '''
    app.run(host='0.0.0.0', port=5000)