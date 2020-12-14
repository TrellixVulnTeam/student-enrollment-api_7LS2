from flask import current_app
from contextlib import closing
import mysql.connector as mysql
import os
from werkzeug.exceptions import ServiceUnavailable


def connection():
    try:
        conn = mysql.connect(host='localhost', user='root', passwd='', port='3306', database='students')
        return conn
    except:
        raise ServiceUnavailable("OOOPS!  we cannot reach the database")


sql = """   CREATE TABLE IF NOT EXISTS `students` (
        `id` int(10) NOT NULL,
        `firstName` varchar(23) NOT NULL,
        `lastName` varchar(23) NOT NULL,
        `clas` varchar(23) NOT NULL,
        `nationality` varchar(100) NOT NULL DEFAULT '1',
        PRIMARY KEY (`id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""

def init_db():
    """Set up the database to stode the user data
    """
    url= os.getenv('DATABASE_URL')
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    
    # with conn as con, con.cursor() as curr:
    #     sql = current_app.open_resource('sql_tables.sql', mode='r') 
    #     curr.execute(sql.read(), multi=True)
    #     con.commit()
    return conn


def init_test_db():
    conn =  mysql.connect(host='localhost', user='root', passwd='', port='3306', database='students_tests')
    # url= os.getenv('DATABASE_URL')
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    return conn

def destroy_db():
    conn = connection()
    curr = conn.cursor()
    students = """DROP TABLE IF EXISTS students CASCADE; """
    queries = [students]
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except:
        print("Fail")



        # host="localhost", user="root", passwd="", port="3306", database="students"