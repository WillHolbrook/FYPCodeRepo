# -*- coding: utf-8 -*-
"""Module fo the UserViewSet"""
from api.serializers.user_serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):  # pylint: disable=too-many-ancestors
    """Users ViewSet to control access"""

    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
