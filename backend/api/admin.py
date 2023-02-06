# -*- coding: utf-8 -*-
"""Used to control what appears in the django admin console"""
from api.models.models import Movie, Rating
from django.contrib import admin

admin.site.register(Movie)
admin.site.register(Rating)
