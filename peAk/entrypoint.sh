#! /bin/bash

set -e

cd /src

# coverage run manage.py test -v 2 && \
# coverage report
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput && \
# python3 manage.py createsuperuser --username toby --password tobyDemo1234! --noinput --email 'blank@email.com'
# ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('toby', 'toby@example.com', 'tobyDemo1234!')"
#python3 load_db.py
python3 manage.py runserver 0.0.0.0:8000


# gunicorn kickstarter_project.wsgi:application -w 3 -b :8000
