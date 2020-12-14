"""
This module defines the base model and associated functions
"""
from datetime import datetime, timedelta
import jwt
import os

from flask import jsonify, make_response

from ...db_config import init_db


class BaseModel(object):
    """
    This class encapsulates the functions of the base model
    that will be shared across all other models
    """

    def __init__(self):
        """initialize the database"""
        self.db = init_db()

    def update_item(self, table, field, data, item_field, item_id):
        """update the field of an item given the item_id"""
        dbconn = self.db
        curr = dbconn.cursor()
        updated = curr.execute("UPDATE {} SET {}='{}' \
                     WHERE {}='{}';".format(table, field, data, item_field, item_id))
        dbconn.commit()
        if updated:
            return True

    def check_exists(self, data):
        """Check if the records exist"""
        curr = self.db.cursor()
        query = "SELECT * FROM students WHERE id={}".format(data)
        curr.execute(query)
        data = curr.fetchone()
        if not data:
            return False
        return True

    def delete_item(self, id):
        """update the field of an item given the item_id"""
        dbconn = self.db
        curr = dbconn.cursor()
        updated = curr.execute("DELETE FROM students WHERE id={};".format(id))
        dbconn.commit()
        return "Done"

    def _type(self):
        """returns the name of the inheriting class"""
        return self.__class__.__name__

    def close_db(self):
        """This function closes the database"""
        self.db.close()
        pass
