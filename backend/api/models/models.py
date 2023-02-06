# -*- coding: utf-8 -*-
"""Movie and Rating models"""
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    """Model to represent a movie containing title and description"""

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_ratings(self) -> int:
        """

        Returns:
            Number of ratings for a film
        """
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self) -> float:
        """

        Returns:
            Average rating for a film
        """
        ratings = Rating.objects.filter(movie=self)
        sum_ratings = 0
        for rating in ratings:
            sum_ratings += rating.stars
        if len(ratings) > 0:
            return sum_ratings / len(ratings)
        return 0.0


class Rating(models.Model):
    """Model to represent a movie rating. Links to a movie, a user and a number of stars"""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        # pylint: disable=all
        # make sure every rating is a unique combination of user and movie

        unique_together = (("user", "movie"),)
        index_together = (("user", "movie"),)
