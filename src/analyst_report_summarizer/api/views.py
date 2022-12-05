from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST', 'GET'])
    def rate_movie(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        user = request.user
        if (request.method == 'POST') and ('stars' in request.data):
            stars = request.data['stars']
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                message = 'Rating Updated'
                code = status.HTTP_200_OK
            except Rating.DoesNotExist:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)

                message = 'Rating Created'
                code = status.HTTP_201_CREATED

            movie = Movie.objects.get(id=pk)
            serializer = RatingSerializer(rating, many=False)
            response = {'message': message, 'result': serializer.data, 'avg_rating': movie.avg_rating()}
            return Response(response, status=code)

        elif request.method == 'POST':
            response = {'message': 'You need to provide Stars When updating or inserting a record'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': f'Rating Retrieved', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except Rating.DoesNotExist:
                return Response(None, status=status.HTTP_204_NO_CONTENT)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class MyRatingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return []

        queryset = self.queryset.filter(user=self.request.user.id)
        return queryset

