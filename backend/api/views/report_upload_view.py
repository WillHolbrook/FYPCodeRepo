# -*- coding: utf-8 -*-
"""View for uploading a new Report"""
from api.serializers.report_details_serializer import ReportDetailSerializer
from api.serializers.report_upload_serializer import UserReportUploadSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserReportUploadView(APIView):
    """API View for uploading a new report"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Method to specify how post requests are handled

        Args:
            request:

        Returns:
            If is a valid file returns the details of the created Report model
            HTTP_400_BAD_REQUEST If there isn't a valid file uploaded
        """
        serializer = UserReportUploadSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            report = serializer.save(user=request.user)
            return Response(
                ReportDetailSerializer(report, context={"request": request}).data
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
