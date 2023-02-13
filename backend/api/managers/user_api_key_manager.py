# -*- coding: utf-8 -*-
"""Module for UserAPIKeyManager"""
import typing

from django.core.exceptions import ValidationError
from rest_framework_api_key.models import BaseAPIKeyManager


class UserAPIKeyManager(BaseAPIKeyManager):
    """Module to manage creation of UserAPIKey objects"""

    def _set_default_values(self, user_profile, is_key1: bool, kwargs):
        """Method to set default values of is_key1"""
        if "name" not in kwargs:
            kwargs["name"] = "AutogenerateName"
        if is_key1 is None:
            keys = self.model.objects.filter(user_profile=user_profile)
            key_bools = [key.is_key1 for key in keys]
            # If there is no key1 generate key 1 else generate key2
            if True in key_bools:
                is_key1 = False
            else:
                is_key1 = True
        return is_key1, kwargs

    def _regenerate_if_required(
        self, user_profile, is_key1: bool = None, regenerate: bool = False
    ):
        """Method to delete key if regenerate is set to True"""
        if regenerate:
            if is_key1 is None:
                raise ValidationError(
                    "Attempted to regenerate key but no key number was given"
                )
            self.model.objects.get(user_profile=user_profile, is_key1=is_key1).delete()

    # pylint: disable=arguments-differ
    def create_key(
        self,
        user_profile,
        is_key1: bool = None,
        regenerate: bool = False,
        **kwargs: typing.Any
    ):
        self._regenerate_if_required(user_profile, is_key1, regenerate)
        is_key1, kwargs = self._set_default_values(user_profile, is_key1, kwargs)
        return super().create_key(user_profile=user_profile, is_key1=is_key1, **kwargs)
