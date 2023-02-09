# -*- coding: utf-8 -*-
"""Used to control what appears in the django admin console"""
# pylint: disable=unused-import
from api.models.profile import Profile
from django.contrib import admin

admin.site.register(Profile)
