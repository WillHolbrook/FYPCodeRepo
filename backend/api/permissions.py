# -*- coding: utf-8 -*-
"""Module for extra unique permissions"""
from api.models.user_api_key import UserAPIKey
from rest_framework_api_key.permissions import BaseHasAPIKey


class HasUserAPIKey(BaseHasAPIKey):
    """Added Authentication method for UserAPIKey"""

    model = UserAPIKey
