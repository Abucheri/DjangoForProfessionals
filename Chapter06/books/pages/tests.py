from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTest(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_url_resolve_homepageview(self):
        resolve_obj = resolve('/')
        self.assertEqual(resolve_obj.func.__name__,
                         HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_url_resolve_aboutpageview(self):
        resolve_obj = resolve(reverse('about'))
        self.assertEqual(resolve_obj.func.__name__,
                         AboutPageView.as_view().__name__)
