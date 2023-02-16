# -*- coding: utf-8 -*-
"""Module for testing UserAPIKey"""
from profile import Profile

from api.models.user_api_key import UserAPIKey
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase


class UserAPIKeyTestCase(TestCase):
    """Tests for user API key"""

    def test_api_key_deletion_with_user(self):
        """Test for API keys getting deleted with associated profile"""
        created_user = get_user_model().objects.create_user("user1", "password")
        profile = created_user.profile
        keys = UserAPIKey.objects.filter(user_profile=profile)
        self.assertEqual(2, len(keys), msg="2 keys were not created for given user")

        (deleted, _) = created_user.delete()
        # 4 objects should be deleted. User, Profile and two keys
        self.assertEqual(4, deleted)
        keys = UserAPIKey.objects.filter(user_profile=profile)
        # When a user is deleted there should be
        self.assertEqual(0, len(keys))

    @staticmethod
    def remove_keys_for_profile(profile: Profile):
        """Method to delete all keys associated with a given profile"""
        keys = UserAPIKey.objects.filter(user_profile=profile)
        # remove any autogenerated keys
        for key in keys:
            key.delete()

    def test_api_key_creation_without_specified_key_number(self):
        """Test for API keys getting created with appropriate key number when not specified"""
        created_user = get_user_model().objects.create_user("user2", "password")
        profile = created_user.profile
        self.remove_keys_for_profile(profile)

        # Check if there are no keys the first key created is key1
        key1, _ = UserAPIKey.objects.create_key(user_profile=profile)
        self.assertEqual(True, key1.is_key1)

        # Check if there is a key1 and no key2 a key2 is created
        key2, _ = UserAPIKey.objects.create_key(user_profile=profile)
        self.assertEqual(False, key2.is_key1)

        # Check if there is a key2 and no key1 a key1 is created
        key1.delete()
        key1, _ = UserAPIKey.objects.create_key(user_profile=profile)
        self.assertEqual(True, key1.is_key1)

    def test_duplicate_key1_generation(self):
        """Test for attempting to generate a duplicate key1"""
        created_user = get_user_model().objects.create_user("user3", "password")
        profile = created_user.profile
        self.remove_keys_for_profile(profile)

        UserAPIKey.objects.create_key(user_profile=profile, is_key1=True)

        with self.assertRaises(ValidationError, msg="Can't generate a duplicate key"):
            UserAPIKey.objects.create_key(user_profile=profile, is_key1=True)

    def test_duplicate_key2_generation(self):
        """Test for attempting to generate a duplicate key1"""
        created_user = get_user_model().objects.create_user("user4", "password")
        profile = created_user.profile
        self.remove_keys_for_profile(profile)

        UserAPIKey.objects.create_key(user_profile=profile, is_key1=False)

        with self.assertRaises(ValidationError, msg="Can't generate a duplicate key"):
            UserAPIKey.objects.create_key(user_profile=profile, is_key1=False)

    def test_key1_regen(self):
        """Test for regenerating key1"""
        created_user = get_user_model().objects.create_user("user5", "password")
        profile = created_user.profile
        self.remove_keys_for_profile(profile)

        _, key1 = UserAPIKey.objects.create_key(user_profile=profile, is_key1=True)

        _, key1_regen = UserAPIKey.objects.create_key(
            user_profile=profile, is_key1=True, regenerate=True
        )

        self.assertNotEqual(key1, key1_regen)

    def test_key2_regen(self):
        """Test for regenerating key2"""
        created_user = get_user_model().objects.create_user("user6", "password")
        profile = created_user.profile
        self.remove_keys_for_profile(profile)

        _, key2 = UserAPIKey.objects.create_key(user_profile=profile, is_key1=False)

        _, key2_regen = UserAPIKey.objects.create_key(
            user_profile=profile, is_key1=False, regenerate=True
        )

        self.assertNotEqual(key2, key2_regen)

    def test_key_regen_no_key_num(self):
        """Test for regenerating key without specifying which one"""
        created_user = get_user_model().objects.create_user("user7", "password")
        profile = created_user.profile

        with self.assertRaises(ValidationError):
            UserAPIKey.objects.create_key(user_profile=profile, regenerate=True)

    def test_api_key_generation_with_profile(self):
        """Test for generation of all required API Keys with a profile"""
        number_of_keys = UserAPIKey.objects.count()
        created_user = get_user_model().objects.create_user("user8", "password")
        self.assertEqual(
            UserAPIKey.objects.count(),
            number_of_keys + 2,
            msg="2 keys not automatically created",
        )
        # If either of the keys aren't generated tge following statements will throw an error
        UserAPIKey.objects.get(user_profile=created_user.profile, is_key1=True)
        UserAPIKey.objects.get(user_profile=created_user.profile, is_key1=False)
        created_user.delete()
