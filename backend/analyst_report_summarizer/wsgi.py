# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position
"""
WSGI config for analyst_report_summarizer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/opt/report_summarizer/API/")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analyst_report_summarizer.settings")

application = get_wsgi_application()
