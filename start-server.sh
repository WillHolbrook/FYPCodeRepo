#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd src/analyst_report_summarizer; python manage.py createsuperuser --no-input)
fi
(cd src/analyst_report_summarizer; gunicorn analyst_report_summarizer.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"