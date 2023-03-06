# -*- coding: utf-8 -*-
"""Template Docstring"""
from api.serializers.profile_serializer import ProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """Template Docstring"""

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "profile")
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }
        depth = 1

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
