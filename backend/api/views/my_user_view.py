# -*- coding: utf-8 -*-
"""Module for MyUserView"""
from api.serializers.user_serializer import UserSerializer
from api.views.auth_utils import check_user_not_anon
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class MyUserView(APIView):
    """View to retrieve user details of the current user"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieves the details of the current user"""
        check_user_not_anon(request)
        return Response(UserSerializer(request.user).data)
