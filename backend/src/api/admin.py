# -*- coding: utf-8 -*-
"""Used to control what appears in the django admin console"""
from django.contrib import admin

from .models import Movie, Rating

admin.site.register(Movie)
admin.site.register(Rating)
