import unittest

from edmontonpy.www.urls import urlpatterns


class TestURLPatterns(unittest.TestCase):
    def setUp(self):
        self.urlpatterns = urlpatterns

    def test_urls(self):
        self.assertEqual(len(urlpatterns), 4)
