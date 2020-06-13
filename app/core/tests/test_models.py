from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """" test creating a new user with an email """

        email = "test@test.com"
        password = '12345678'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if email for a new user is normalized"""

        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password="123@123"
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """"Test that creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="123@123"
            )

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "test@123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
