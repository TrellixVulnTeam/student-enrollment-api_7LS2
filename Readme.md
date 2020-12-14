# RESTFul API Implementation and continuous deployment 

This is a Python Flask framework API project

Integration with Flask-restplus, Flask-Cors, MySQL.

### Enpoints:

The project has a total of five endpoints

- GET all students`GET /api/students`

- POST a student: `POST /api/students`

- GET all students in a class `GET /api/students/fetchstudent?class=`

- GET a single student `GET /api/students/fetchstudent?id=`

- PUT edit a student data `PUT /api/students/<int:id>`

- DELETE a student Record  `DELETE /api/students/<int:id>`



## Installation

### Setting up the Python Flask API

Create a project directory
`$ mkdir Project`
`$ cd Project`

Clone the project
`$ git clone project url .`

Install Virtual environment
`$ pip install virtualenv`

Create a virtual environment 
`$ virtualenv env   `

Activate virtual environment
On windows 
`env\Scripts\activate`

On MacOs/Linux
`source env/bin/activate`

Install with pip project dependencies :

```
$ pip install -r requirements.txt
```

Export project environment Variables
```
export FLASK_APP="run.py"
export APP_SETTINGS="development"
export DATABASE_URL="host="localhost", user="<dbuser>", passwd="<your password>", port="3306", database="students""
export DATABASE_TEST_URL="host="localhost", user="<dbuser>", passwd="<your password>", port="3306", database="students_tests""
```

### Setting up the DB

Install any mysql server on your machine; xampp, wamp, lamp etc
Create a database `students` and `students_tests`


## Run the app

```
$ flask run
```

### Setting up POSTMAN

Open your postman app on your machine and import `student.postman_collection.json`



## Running tests

I have use nosetest as a test runner in this case
```
$ nosetests --with-coverage --cover-package=app app -v
```

The output

```
app.test.base_tests.init_test_db ... ok
Test that a user cannot add same student twice ... ok
Test that a user can add new student using a POST request ... ok
Test deleting a student that doest exist data using a PUT request ... ok
Test deleting a student data using a PUT request ... ok
Test editing a student that doest exist data using a PUT request ... ok
Test editing a student data using a PUT request ... ok
Test get a students using a GET request ... ok
Test get all students in a class using a GET request ... ok

Name                            Stmts   Miss  Cover
---------------------------------------------------
app\__init__.py                    51     22    57%
app\api\__init__.py                 0      0   100%
app\api\v1\__init__.py              7      0   100%
app\api\v1\base_model.py           34      5    85%
app\api\v1\serializers.py           4      0   100%
app\api\v1\students.py             72      9    88%
app\api\v1\students_models.py      51     10    80%
app\db_config.py                   34      4    88%
---------------------------------------------------
TOTAL                             253     50    80%
----------------------------------------------------------------------
Ran 9 tests in 0.817s

OK
```

THANK YOU 