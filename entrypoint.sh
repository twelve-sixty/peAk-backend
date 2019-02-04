#! /bin/bash

set -e

cd /src

# coverage run manage.py test -v 2 && \
# coverage report
python3 ./peAk/manage.py makemigrations --noinput
python3 ./peAk/manage.py migrate --noinput
python3 ./peAk/manage.py collectstatic --noinput && \
# python3 load_db.py
python3 ./peAk/manage.py runserver 0.0.0.0:8000

# gunicorn kickstarter_project.wsgi:application -w 3 -b :8000
