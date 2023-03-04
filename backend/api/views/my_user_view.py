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
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        """Method to update user details"""
        check_user_not_anon(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user: get_user_model() = request.user
            user.set_password(serializer.validated_data["password"])
            user.username = serializer.validated_data["username"]
            user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request):
        """Method to delete a logged in user"""
        check_user_not_anon(request)
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
