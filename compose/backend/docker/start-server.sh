#!/usr/bin/env bash
# start-server.sh
(cd opt/app || exit; python manage.py makemigrations);
(cd opt/app || exit; python manage.py migrate);
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd opt/app || exit; python manage.py createsuperuser --no-input);
fi
(cd opt/app || exit; python manage.py runserver '0.0.0.0:8000');
