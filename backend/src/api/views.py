# -*- coding: utf-8 -*-
# pylint: disable=too-many-ancestors
"""Views used in basic app"""
import time

from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Users ViewSet to control access"""

    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Movie ViewSet, with custom method to rate a movie with a debug option for listing them"""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    debug = False
    list_delay = False

    # Used to test error and loading pages artificially
    def list(self, request, *args, **kwargs):
        """Template Docstring"""
        if MovieViewSet.debug:
            time.sleep(5)
        if MovieViewSet.list_delay:
            return super().list(request, *args, **kwargs)
        return Response(
            {"message": "internal Server Error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    @action(detail=True, methods=["POST", "GET"])
    def rate_movie(self, request, primary_key=None):
        """Template Docstring"""
        movie = Movie.objects.get(id=primary_key)
        user = request.user
        if (request.method == "POST") and ("stars" in request.data):
            stars = request.data["stars"]
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                message = "Rating Updated"
                code = status.HTTP_200_OK
            except Rating.DoesNotExist:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)

                message = "Rating Created"
                code = status.HTTP_201_CREATED

            movie = Movie.objects.get(id=primary_key)
            serializer = RatingSerializer(rating, many=False)
            response = {
                "message": message,
                "result": serializer.data,
                "avg_rating": movie.avg_rating(),
                "no_of_ratings": movie.no_of_ratings(),
            }
            return Response(response, status=code)

        if request.method == "POST":
            response = {
                "message": "You need to provide Stars When updating or inserting a record"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            rating = Rating.objects.get(user=user.id, movie=movie.id)
            serializer = RatingSerializer(rating, many=False)
            response = {"message": "Rating Retrieved", "result": serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Rating.DoesNotExist:
            return Response(None, status=status.HTTP_204_NO_CONTENT)


class RatingViewSet(viewsets.ModelViewSet):
    """Template Docstring"""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class MyRatingsViewSet(viewsets.ReadOnlyModelViewSet):
    """Template Docstring"""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return []

        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset
