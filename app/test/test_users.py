# !/usr/bin/env python3

import unittest
import os
import json
from ..db import db


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.users = {'username': 'johndoe', 'password': 'test123'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        res = self.client().post('/users/', data=self.users)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Borabora', str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()