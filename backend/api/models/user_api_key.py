# -*- coding: utf-8 -*-
"""Module for UserAPIKey Model and associated methods"""
from api.managers.user_api_key_manager import UserAPIKeyManager
from api.models.profile import Profile
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_api_key.models import AbstractAPIKey


class UserAPIKey(AbstractAPIKey):
    """Custom API key for a User"""

    objects = UserAPIKeyManager()

    max_num_api_keys: int = 2
    regen: bool = False

    class Meta(AbstractAPIKey.Meta):
        verbose_name = "User API key"
        verbose_name_plural = "User API keys"

    is_key1 = models.BooleanField(null=True)

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )

    @receiver(post_save, sender=Profile)
    def auto_generate_keys(
        sender, instance, created, **kwargs
    ):  # pylint: disable=[no-self-argument, unused-argument]
        """Method to auto generate api keys on user creation"""
        if created:
            UserAPIKey.objects.create_key(user_profile=instance, is_key1=True)
            UserAPIKey.objects.create_key(user_profile=instance, is_key1=False)

    def clean(self) -> None:
        if UserAPIKey.objects.filter(
            user_profile=self.user_profile, is_key1=self.is_key1
        ).exists():
            key_num = self.max_num_api_keys - int(bool(self.is_key1))
            raise ValidationError(
                f"A single user can't have multiple API Keys for Key{key_num} "
                f"if you want to have another value for Key{key_num} delete the "
                f"old key before creating the new one"
            )
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
