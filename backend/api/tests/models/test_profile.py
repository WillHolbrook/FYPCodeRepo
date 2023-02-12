# -*- coding: utf-8 -*-
"""Module for testing Profile model"""
import io
import sys
from pathlib import Path

from api.models.profile import Profile
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase
from PIL import Image


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
        created_user.delete()

    @staticmethod
    def _load_test_image(
        path: Path = Path("./api/tests/resources/test.jpg"),
    ) -> InMemoryUploadedFile:
        image = Image.open(path)
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=85)
        output.seek(0)
        return InMemoryUploadedFile(
            output,
            "ImageField",
            path.name,
            "image/jpeg",
            sys.getsizeof(output),
            None,
        )

    def test_profile_picture_upload(self):
        """Test for Profile picture upload"""
        created_user = get_user_model().objects.create_user("user3", "password")
        created_profile: Profile = Profile.objects.get(user=created_user.id)

        created_profile.profile_image = self._load_test_image()
        created_profile.save()

        retrieved_profile = Profile.objects.get(user=created_user.id)
        self.assertIsNotNone(retrieved_profile.profile_image.file)
        created_user.delete()

    def test_profile_picture_resizing(self):
        """Test for resizing of uploaded profile picture"""
        created_user = get_user_model().objects.create_user("user4", "password")
        created_profile: Profile = Profile.objects.get(user=created_user.id)

        created_profile.profile_image = self._load_test_image()
        created_profile.save()

        retrieved_profile = Profile.objects.get(user=created_user.id)
        self.assertIsNotNone(retrieved_profile.profile_image.file)

        self.assertEqual(
            Profile.profile_image_size[0], retrieved_profile.profile_image.width
        )
        self.assertEqual(
            Profile.profile_image_size[1], retrieved_profile.profile_image.height
        )

        created_user.delete()

    def test_profile_deletion_when_user_removed(self):
        """Test for Profile Deletion"""
        # get a user and matching profile
        created_user = get_user_model().objects.create_user("user4", "password")
        profile = created_user.profile

        self.assertIsNotNone(profile, msg="No profile found for user")
        (deleted, _) = created_user.delete()
        # at least 2 Items should be deleted from the database, not just one
        self.assertGreaterEqual(deleted, 2)
        # attempt to re-fetch profile from the database (should fail)
        with self.assertRaises(
            ObjectDoesNotExist, msg="Profile not removed from DB when user deleted"
        ):
            Profile.objects.get(pk=profile.pk)
