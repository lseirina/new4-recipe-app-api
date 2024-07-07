#!/bin/sh

set -e # if ine command fails - all commands fail

python manage.py wait_for_db
python manage.py collectstatic --noinput # collect all static and media files from different apps to one file
python manage.py migrate

# it is a command to run uwsgi, workers handle request
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi