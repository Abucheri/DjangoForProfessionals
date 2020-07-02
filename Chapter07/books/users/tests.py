from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password='testpass123',
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superwill',
            email='superwill@gmail.com',
            password='testpass123',
        )
        self.assertEqual(admin_user.username, 'superwill')
        self.assertEqual(admin_user.email, 'superwill@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTest(TestCase):

    username = 'newuser'
    email = 'newuser@gmail.com'

    def setUp(self):
        self.response = self.client.get(reverse('account_signup'))

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        get_user_model().objects.create_user(
            self.username,
            self.email
        )
        users_query = get_user_model().objects
        self.assertEqual(users_query.count(), 1)
        self.assertEqual(users_query.all()[0].email, self.email)
        self.assertEqual(users_query.all()[0].username, self.username)
