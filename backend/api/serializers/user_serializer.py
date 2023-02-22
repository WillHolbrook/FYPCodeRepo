# -*- coding: utf-8 -*-
"""Template Docstring"""
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Template Docstring"""

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
