
import unittest
import json
import string
from contextlib import closing
from random import choice, randint

# local imports
from .. import create_app
from ..db_config import destroy_db, init_db

from .base_tests import BaseTest


class TestStudents(BaseTest):
    """This class collects all the test cases for the stdents"""

    def test_adding_students(self):
        """Test that a user can add new student using a POST request"""
        record = self.post_students()
        self.assertEqual(record.status_code, 201)
        self.assertEqual(record.json['issuccess'], True)

    def test_adding_student_adding_dublicate_student(self):
        """Test that a user cannot add same student twice"""
        record = self.post_students()
        record2 = self.post_students()
        self.assertEqual(record2.status_code, 200)
        # self.assertEqual(record.json['issuccess'], False)

    def test_getting_students(self):
        """Test get all students using a GET request"""
        post = self.post_students()
        get = self.get(path="/api/students")
        self.assertEqual(get.status_code, 200)
        self.assertEqual(get.json['issuccess'], True)

    def test_getting_students(self):
        """Test get all students in a class using a GET request"""
        post = self.post_students()
        get = self.get(path="api/students/fetchstudent?class=3A")
        self.assertEqual(get.status_code, 200)
        self.assertEqual(get.json['issuccess'], True)

    def test_getting_student(self):
        """Test get a students using a GET request"""
        post = self.post_students()
        path = "api/students/fetchstudent?id={}".format(self.student['id'])
        get = self.get(path=path)
        self.assertEqual(get.status_code, 200)
        self.assertEqual(get.json['issuccess'], True)


    def test_editing_student(self):
        """Test editing a student data using a PUT request"""
        post = self.post_students()
        path = "/api/students/{}".format(self.student['id'])
        data= {"nationality" : "Canada"}
        put = self.put(path=path, data=data)
        self.assertEqual(put.json['message'], "Successfully Updated")
        self.assertEqual(put.status_code, 200)

    def test_editing_not_exist_student(self):
        """Test editing a student that doest exist data using a PUT request"""
        post = self.post_students()
        path = "/api/students/1234"
        data= {"nationality" : "Canada"}
        put = self.put(path=path, data=data)
        self.assertEqual(put.json['message'], "student does not exist")
        self.assertEqual(put.status_code, 400)

    def test_deleting_student(self):
        """Test deleting a student data using a PUT request"""
        post = self.post_students()
        path = "/api/students/{}".format(self.student['id'])
        delete = self.delete(path=path)
        self.assertEqual(delete.json['message'], "Successfully deleted")
        self.assertEqual(delete.status_code, 200)

    def test_deleting_not_exist_student(self):
        """Test deleting a student that doest exist data using a PUT request"""
        post = self.post_students()
        path = "/api/students/1234"
        delete = self.delete(path=path)
        self.assertEqual(delete.json['message'], "student does not exist")
        self.assertEqual(delete.status_code, 400)
   

    def tearDown(self):
        """This function destroys objests created during the test run"""

        with self.app.app_context():
            destroy_db()
            # self.db.close()


if __name__ == "__main__":
    unittest.main()