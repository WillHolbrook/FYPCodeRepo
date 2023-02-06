# -*- coding: utf-8 -*-
"""Template Docstring"""
from django.urls import include, path
from rest_framework import routers

from .views import MovieViewSet, MyRatingsViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("ratings", RatingViewSet)
router.register("myratings", MyRatingsViewSet)
router.register("users", UserViewSet)


urlpatterns = [path("", include(router.urls))]
