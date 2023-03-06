# -*- coding: utf-8 -*-
"""Module for Serialization of a Profile"""
from api.models.profile import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for uploading a Profile Picture"""

    profile_image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Profile
        fields = [
            "profile_image",
        ]
