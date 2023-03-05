# -*- coding: utf-8 -*-
"""Module to contain Profile Model and associated methods"""
import io
import sys

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    """Intermediary model for proxying built in user"""

    profile_image_size = (500, 500)

    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="profile"
    )

    profile_image = models.ImageField(
        upload_to="profile_pictures/%Y/%m", default=None, null=True
    )

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

    def save(self, *args, **kwargs):
        if self.profile_image:
            image = Image.open(self.profile_image)
            image = image.convert("RGB")
            image = image.resize(Profile.profile_image_size, Image.ANTIALIAS)
            output = io.BytesIO()
            image.save(output, format="JPEG", quality=85)
            output.seek(0)
            self.profile_image = InMemoryUploadedFile(
                output,
                "ImageField",
                self.profile_image.name,
                "image/jpeg",
                sys.getsizeof(output),
                None,
            )

        super().save(*args, **kwargs)
