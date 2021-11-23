"""docstring"""
from django.test import TestCase

class SmokeTest(TestCase):
    """docstring"""


    def test_bad_maths(self):
        """docstring"""
        self.assertEqual(1 + 1, 3)
