# -*- coding: utf-8 -*-
"""Template Docstring"""
from api.views.add_report_to_corpus_view import AddReportToCorpusView
from api.views.calculate_idf_view import CalculateIDF
from api.views.extract_plaintext_view import ExtractPlaintextView
from api.views.extract_sentence_bert_view import ReportExtractSentenceBertView
from api.views.extract_sentence_tfidf_view import UserReportExtractSentenceView
from api.views.my_user_view import MyUserView
from api.views.profile_view import ProfileView
from api.views.report_upload_view import UserReportUploadView
from api.views.report_viewset import ReportViewSet
from api.views.user_view_set import UserViewSet
from django.urls import include, path, re_path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("reports", ReportViewSet, basename="reports")

api_patterns = [
    re_path("report_upload", UserReportUploadView.as_view(), name="report_upload"),
    re_path(
        "report_extract_sentence/(?P<report_pk>[0-9]*)",
        UserReportExtractSentenceView.as_view(),
        name="extract_sentence",
    ),
    re_path(
        "report_extract_sentence_bert/(?P<report_pk>[0-9]*)",
        ReportExtractSentenceBertView.as_view(),
        name="extract_sentence_bert",
    ),
    re_path(
        "add_to_corpus/(?P<report_pk>[0-9]*)",
        AddReportToCorpusView.as_view(),
        name="add_to_corpus",
    ),
    re_path(
        "extract_plaintext/(?P<report_pk>[0-9]*)",
        ExtractPlaintextView.as_view(),
        name="extract_plaintext",
    ),
    re_path("profile", ProfileView.as_view(), name="profile"),
    re_path("calculate_idf", CalculateIDF.as_view(), name="calculate_idf"),
    re_path("user", MyUserView.as_view(), name="my_user"),
]


urlpatterns = [
    path("", include(router.urls)),
    path("", include(api_patterns)),
]
