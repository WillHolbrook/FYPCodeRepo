# -*- coding: utf-8 -*-
"""Module for testing Profile model"""
from api.models.profile import Profile
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase


class ProfileTestCase(TestCase):
    """Tests for profile"""

    def test_profile_creation(self):
        """Test for Profile Creation"""
        number_of_profiles = Profile.objects.count()
        created_user = get_user_model().objects.create_user("user2", "password")
        self.assertEqual(
            created_user.username,
            "user2",
            msg="Username not correctly set at user creation",
        )
        self.assertEqual(
            Profile.objects.count(),
            number_of_profiles + 1,
            msg="Profile not automatically created",
        )

    # TODO
    def test_profile_picture_upload(self):
        """Test for Profile picture upload"""

    # TODO
    def test_profile_picture_resizing(self):
        """Test for resizing of uploaded profile picture"""

    # TODO
    def test_api_key_generation_with_profile(self):
        """Test for generation of all required API Keys with a profile"""

    def test_profile_deletion_when_user_removed(self):
        """Test for Profile Deletion"""
        # get a user and matching profile
        user = get_user_model().objects.get(pk=1)
        profile = user.profile

        self.assertIsNotNone(profile, msg="No profile found for user")
        (deleted, _) = user.delete()
        # 2 Items should be deleted from the database, not just one
        self.assertEqual(deleted, 2)
        # attempt to refetch profile from the database (should fail)
        with self.assertRaises(
            ObjectDoesNotExist, msg="Profile not removed from DB when user deleted"
        ):
            Profile.objects.get(pk=profile.pk)
