# -*- coding: utf-8 -*-
"""Module for MyUserView"""
from api.serializers.user_serializer import UserSerializer
from api.views.auth_utils import check_user_not_anon
from django.contrib.auth import get_user_model
from rest_framework import status
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
        return Response(UserSerializer(request.user, context={"request": request}).data)

    def put(self, request):
        """Method to update user details"""
        check_user_not_anon(request)
        if request.data.get("password") is not None:
            user: get_user_model() = request.user
            user.set_password(request.data.get("password"))
            if request.data.get("username") is not None:
                user.username = request.data.get("username")
            user.save()
            return Response(
                data=UserSerializer(user, context={"request": request}).data,
                status=status.HTTP_200_OK,
            )
        return Response(
            data={"error": "password must not be none"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request):
        """Method to delete a logged in user"""
        check_user_not_anon(request)
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
