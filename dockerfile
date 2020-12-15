# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP="run.py"
ENV APP_SETTINGS="development"
ENV DATABASE_TEST_URL="host='localhost', user='root', passwd=', port='3306', database='students_test'"
ENV DATABASE_URL=host="host='localhost', user='root', passwd=', port='3306', database='students'"
ENV SECRET_KEY="mcogol"
ENV FLASK_DEBUG=1


COPY . /app
# install dependencies
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

RUN \
 apk add  postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps


# copy project


EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "-w", "4", "run:app"]