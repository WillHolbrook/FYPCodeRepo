# -*- coding: utf-8 -*-
"""Module for utils for checking auth in views"""
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
