#!/bin/sh

set -e

case "$1" in
    web)
        python manage.py flush --no-input
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver 0.0.0.0:8000
        ;;
    celery)
        celery -A config worker --loglevel=info -P eventlet
        ;;
    *)
        exec "$@"
esac