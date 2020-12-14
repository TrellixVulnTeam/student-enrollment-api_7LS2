
# Adding resources to the api
from flask_restplus import Api
from flask import Blueprint
from werkzeug.exceptions import NotFound

version_one = Blueprint('version1', __name__, url_prefix="/api")

from .students import api as stu

api = Api(version_one,
          title=' Students API ',
          version='1.0',
          description="")

api.add_namespace(stu, path="/students")

