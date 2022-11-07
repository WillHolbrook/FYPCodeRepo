from django.urls import path
from django.views.generic import TemplateView

from .api import ListApi, CardApi

urlpatterns = [
    path('lists', ListApi.as_view()),
    path('cards', CardApi.as_view()),
    path('home', TemplateView.as_view(template_name="summarizer_web_app/home.html"))
]
