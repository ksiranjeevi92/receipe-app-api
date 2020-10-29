from django.test import  TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        '''Test Create user with email address'''
        email = 'test@test.com'
        password = 'password'

        user= get_user_model().objects.create_user(
        email = email,
        password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        '''test user email address is normalized'''
        email = 'test@TEST.com'
        password = 'password'

        user= get_user_model().objects.create_user(
         email,
         password
        )
        self.assertEqual(user.email,email.lower())
