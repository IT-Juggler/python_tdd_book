"""docstring"""
from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):
    """docstring"""


    def test_home_page_returns_correct_html(self):
        """Check the html."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_can_save_a_post_request(self):
        """Check for successful POST."""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


class ItemModelTest(TestCase):
    """docstring"""

    def test_saving_and_retrieving_items(self):
        """docstring"""
        first_item = Item()
        