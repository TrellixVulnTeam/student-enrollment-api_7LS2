"""
This module collects all the Data Transfer Objects for the API
"""
from flask_restplus import Namespace, fields


class StudentsDTO(object):
    """ dockstring for the asset module """
    api = Namespace('Students', description='Students resources')
    n_data = api.model('new student request', {
        'id': fields.Integer(required=True, description="student ID"),
        'firstName': fields.String(required=True, description="First Name of the student"),
        'lastName': fields.String(required=True, description="Last Name of the student"),
        'class': fields.String(required=True, description="class of the student"),
        'nationality': fields.String(required=True, description="nationality of the student")
    })
