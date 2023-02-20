# -*- coding: utf-8 -*-
"""Template Docstring"""
from api.views.user_report_extract_sentence_view import UserReportExtractSentenceView
from api.views.user_report_upload_view import UserReportUploadView
from api.views.user_report_view import ReportViewSet
from api.views.user_view_set import UserViewSet
from django.urls import include, path, re_path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("reports", ReportViewSet)

api_patterns = [
    re_path("report_upload", UserReportUploadView.as_view(), name="report_upload"),
    re_path(
        "report_extract_sentence/(?P<report_pk>[0-9]*)",
        UserReportExtractSentenceView.as_view(),
        name="extract_sentence",
    ),
]


urlpatterns = [
    path("", include(router.urls)),
    path("", include(api_patterns)),
]
