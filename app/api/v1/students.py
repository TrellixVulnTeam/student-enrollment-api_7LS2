import os
import re
import json
import string
import werkzeug
from random import randint
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden, Conflict

from flask_restplus import Resource, reqparse
from flask import jsonify, make_response, request, g, jsonify, redirect, url_for

from .serializers import StudentsDTO
from .students_models import studentsModel 



api = StudentsDTO().api
n_data = StudentsDTO().n_data


########################################################################## POST AND GET students #########################################################################################

# Adding students 
@api.route("/")
class Students(Resource):
    @api.expect(n_data, validate=True) 
    def post(self):
        req_data = request.data.decode().replace("'", '"')
        if not req_data:
            raise BadRequest("Provide data in the request")
        body = json.loads(req_data)
        try:
            id = body['id']
            firstName = body['firstName']
            lastName = body['lastName']
            clas = body['class']
            nationality = body['nationality']
        except (KeyError, IndexError) as e:
            raise BadRequest
        
        data = {
            "idd" : id,
            "firstName" : firstName,
            "lastName" : lastName,
            "clas" : clas,
            "nationality" : nationality
        }
        stdu = studentsModel(**data)
        if stdu.check_exists(data=data['idd']) == False:
            stdu = studentsModel(**data)
            resp = stdu.save()  
            return {
                "message": resp,
                "issuccess" : True
            },201
        else:
            return {
                "message" : "student with id {} exist".format(data['idd']),
                "issuccess" : False
            }, 200

# Get students 

    def get(self):
        resp = studentsModel().get_students()
        return resp, 200
        

########################################################################## ______________ #########################################################################################

@api.route("/fetchstudent")
class StudentSpec(Resource):

    def get(self):
        if not request.args:
            raise BadRequest("Url params are are needed")
        try:
            id = request.args.get('id')
            clas = request.args.get('class')
        except (KeyError, IndexError) as e:
            raise BadRequest("expecting id and/or class")
    
        if request.args.get('class'):     
            resp = studentsModel().fetch_students_class(clas)
            return resp, 200

        elif request.args.get('id'):
            resp = studentsModel().fetch_student(request.args.get('id'))
            return resp, 200
        
        
        


# PUT and DELETE endpoints
@api.route("/<int:id>")
class StudentAction(Resource):

    def put(self, id):
        if studentsModel().check_exists(data=id) == False:
            raise BadRequest("student does not exist")

        req_data = request.data.decode().replace("'", '"')
        if not req_data:
            raise BadRequest("Provide data in the request")
        body = json.loads(req_data)
        for field, value in body.items(): 
            studentsModel().update_item(table="students",field=field,data=value,item_field="id",item_id=id)

        updated = {"message" : "Successfully Updated"}
        return updated, 200



    def delete(self, id):
        if studentsModel().check_exists(data=id) == False:
            raise BadRequest("student does not exist")
        
        studentsModel().delete_item(id)
        return {
            "message" : "Successfully deleted",
            "issucess" : True
        },200