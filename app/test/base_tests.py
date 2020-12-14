import unittest
import json
import string
from contextlib import closing
from random import choice, randint

# local imports
from .. import create_app
from ..db_config import destroy_db, init_test_db


class BaseTest(unittest.TestCase):
    """docstring for BaseTest"""
    api_prefix = "/api/"

    def setUp(self):
        """Performs variable definition and app initialization"""
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.student = {
            "id":11921,
            "firstName": "Mike",
            "lastName": "Wong",
            "class":"3A",
            "nationality": "Singapore"
        } 


        self.error_msg = "The path accessed / resource requested cannot be found, please check"

        with self.app.app_context():
            self.db = init_test_db()

    def endpoint_path(self, path):
        return "/api" + path

    def post(self, path, data, auth):
        """ Make API calls for the POST method"""
        paths = self.endpoint_path(path=path)
        dto = json.dumps(data)
        res = self.client.post(path=path, data=dto, content_type='application/json')
        return res

    def get(self, path):
        """ Make API calls for the POST method"""
        res = self.client.get(path=path, content_type='application/json')
        return res

    def put(self, path, data):
        """ Make API calls for the POST method"""
        paths = self.endpoint_path(path=path)
        dto = json.dumps(data)
        res = self.client.put(path=path, data=dto, content_type='application/json')
        return res

    def delete(self, path):
        """ Make API calls for the POST method"""
        res = self.client.delete(path=path,  content_type='application/json')
        return res

    def post_students(self):
        res = self.post(path="/api/students", data=self.student, auth=None)
        return res