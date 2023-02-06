# -*- coding: utf-8 -*-
"""Template Docstring"""
from api.views.views import MovieViewSet, MyRatingsViewSet, RatingViewSet, UserViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("ratings", RatingViewSet)
router.register("myratings", MyRatingsViewSet)
router.register("users", UserViewSet)


urlpatterns = [path("", include(router.urls))]
