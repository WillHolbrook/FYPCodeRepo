# -*- coding: utf-8 -*-
"""Module for utils for checking auth in views"""
from __future__ import annotations

from api.models.report import Report
from rest_framework import status
from rest_framework.response import Response


def check_user_not_anon(request):
    """Function to check if a user in a request is anonymous and if so return an error Response"""
    if request.user.is_anonymous:
        return Response(
            data={"message": "User can't be anonymous"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    return None


def check_user_is_present_and_has_access_to_given_report(
    request, report_pk: int
) -> tuple[Response, None] | tuple[None, Report]:
    """
    Method to check if a user is present and has access to a given report

    Args:
        request:
        report_pk: The Primary Key of the Report to extract

    Returns:
        error Response, None - if the user isn't provided or the specified report
            doesn't exist/they don't own the report
        None, Report - If the user is provided, and they have access to the specified report
    """
    user_anon_resp = check_user_not_anon(request)
    if user_anon_resp:
        return user_anon_resp, None
    try:
        report = Report.objects.get(pk=report_pk, user=request.user.id)
        return None, report
    except Report.DoesNotExist:
        return (
            Response(
                data={"message": "Report doesn't exist"},
                status=status.HTTP_404_NOT_FOUND,
            ),
            None,
        )
