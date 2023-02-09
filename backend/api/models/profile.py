# -*- coding: utf-8 -*-
"""Module to contain Profile Model and associated methods"""
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Intermediary model for proxying built in user"""

    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )

    # api_key_1 = models.OneToOneField()

    @receiver(post_save, sender=get_user_model())
    def create_user_profile(
        sender, instance, created, **kwargs
    ):  # pylint: disable=[no-self-argument, unused-argument]
        """Creates a Profile whenever a User is Saved"""
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=get_user_model())
    def save_user_profile(
        sender, instance, **kwargs
    ):  # pylint: disable=[no-self-argument, unused-argument]
        """Saves a Profile object whenever a User is saved"""
        instance.profile.save()
