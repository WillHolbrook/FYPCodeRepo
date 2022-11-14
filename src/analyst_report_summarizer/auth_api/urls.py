from django.urls import path

from .api import LoginView, LogoutView

urlpatterns = [
    path(r'login/', LoginView.as_view()),
    path(r'logout/', LogoutView.as_view()),
]
