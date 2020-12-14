from flask import send_file, send_from_directory, jsonify, url_for, request

from ...db_config import init_db
from .base_model import BaseModel


class studentsModel(BaseModel):
    """This class encapsulates the functions of the user model"""

    def __init__(self, idd="", firstName="", lastName="", clas="", nationality=""):
        """initialize the user model"""
        self.idd = idd
        self.firstName = firstName
        self.lastName = lastName
        self.clas = clas
        self.nationality = nationality
        self.db = init_db()
        self.cur = self.db.cursor()
    
    def get_students(self):
        query = """SELECT id, firstName, lastName, clas, nationality
                  FROM students  """ 
        self.cur.execute(query)
        data = self.cur.fetchall()
        resp = []
        self.cur.close()

        for i, items in enumerate(data):
            id, firstName, lastName, clas, nationality  = items
            
            students = {
                "id" : id,
                "firstName" : firstName,
                "lastName" : lastName,
                "class" : clas,
                "nationality" : nationality
            }
            resp.append(students)
        return {
            "issuccess": True,
            "quantity" : len(resp),
            "students" : resp
        }

    def fetch_students_class(self, clas=""):
        query = "SELECT id, firstName, lastName, clas, nationality FROM students WHERE clas='{}'".format(clas) 
        self.cur.execute(query)
        data = self.cur.fetchall()
        self.cur.close()
        resp = []
        for i, items in enumerate(data):
            id, firstName, lastName, clas, nationality  = items
            
            students = {
                "id" : id,
                "firstName" : firstName,
                "lastName" : lastName,
                "class" : clas,
                "nationality" : nationality
            }
            resp.append(students)
        return {
            "issuccess": True,
            "quantity" : len(resp),
            "students" : resp
        }

    def fetch_student(self, id=""):
        query = "SELECT id, firstName, lastName, clas, nationality FROM students WHERE id='{}'".format(id) 
        self.cur.execute(query)
        data = self.cur.fetchone()
        self.cur.close()
        resp = []
        
        id, firstName, lastName, clas, nationality  = data
            
        student = {
            "id" : id,
            "firstName" : firstName,
            "lastName" : lastName,
            "class" : clas,
            "nationality" : nationality
        }
        resp.append(student)
        return {
            "issuccess": True,
            "quantity" : len(resp),
            "students" : resp
        }

    def save(self):
        """Add student details to the database"""
        student = {
            "id": self.idd,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "clas" : self.clas, 
            "nationality" : self.nationality
        }

        query = """INSERT INTO students (id, firstName, lastName, clas, nationality) \
                    VALUES (%(id)s, %(firstName)s, %(lastName)s, %(clas)s, %(nationality)s);
                """
        self.cur.execute(query, student)
        self.db.commit()
        self.cur.close()
        return "{} was uccessfully added".format(self.firstName)

