# -*- coding: utf-8 -*-
"""Module for UserReportExtractSentenceView"""
from api.models.profile import Profile
from api.serializers.profile_serializer import ProfileSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfileView(APIView):
    """View to update and retrieve profile information"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer

    def post(self, request):
        """
        Method to specify how post requests are handled

        Args:
           request:

        Returns:
           If required profile fields are provided returns the details of the updated Profile
           HTTP_400_BAD_REQUEST If required profile fields aren't provided
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile: Profile = request.user.profile
            profile: Profile = serializer.update(profile, serializer.validated_data)

            return Response(ProfileSerializer(profile).data)

        return Response(
            data={"message": "required profile fields aren't provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def get(self, request):
        """Retrieves the profile details of the specified user"""
        return Response(ProfileSerializer(Profile.objects.get(user=request.user)).data)
