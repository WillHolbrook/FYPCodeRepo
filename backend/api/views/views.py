# -*- coding: utf-8 -*-
# pylint: disable=too-many-ancestors
"""Views used in basic app"""

from api.serializers.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    """Users ViewSet to control access"""

    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
