#!/bin/sh

./manage.py migrate
./manage.py collectstatic --noinput
export DJANGO_SETTINGS_MODEL=running
gunicorn -b 0.0.0.0 -p 8000 running.wsgi:application --daemon
