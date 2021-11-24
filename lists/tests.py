"""docstring"""
from django.test import TestCase


class HomePageTest(TestCase):
    """docstring"""


    def test_home_page_returns_correct_html(self):
        """Check the html."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
