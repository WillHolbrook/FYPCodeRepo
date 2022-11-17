from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('minibooks', views.MiniBookViewSet)

urlpatterns = [
    path('1', views.first),
    path('2', views.Another.as_view()),
    path('', include(router.get_urls()))
]
