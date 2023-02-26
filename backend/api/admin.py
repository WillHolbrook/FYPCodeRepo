# -*- coding: utf-8 -*-
"""Used to control what appears in the django admin console"""
from api.models.profile import Profile
from api.models.report import Report
from api.models.sentence import Sentence
from api.models.term_idf import TermIDF
from api.models.user_api_key import UserAPIKey
from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin

admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Sentence)
admin.site.register(TermIDF)


@admin.register(UserAPIKey)
class OrganizationAPIKeyModelAdmin(APIKeyModelAdmin):
    """Class to allow management of UserAPIKeys through Admin UI"""
