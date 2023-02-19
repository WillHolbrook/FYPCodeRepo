# -*- coding: utf-8 -*-
"""Template Docstring"""
from api.views.user_report_upload_view import UserReportUploadView
from api.views.user_report_view import ReportViewSet
from api.views.user_view_set import UserViewSet
from django.urls import include, path, re_path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("reports", ReportViewSet)

api_patterns = [re_path("report_upload", UserReportUploadView.as_view())]


urlpatterns = [
    path("", include(router.urls)),
    path("", include(api_patterns)),
]
