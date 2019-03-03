import unittest

from django.apps import AppConfig


class AppConfigTest(unittest.TestCase):
    EXPECTED_NAME = None
    APP_CONFIG_CLASS = None

    def setUp(self):
        if self.EXPECTED_NAME and self.APP_CONFIG_CLASS is not None:
            self.expected_name = self.EXPECTED_NAME
            self.app_config_class = self.APP_CONFIG_CLASS

    def test_appconfig(self):
        if self.APP_CONFIG_CLASS is not None:
            self.assertTrue(issubclass(self.app_config_class, AppConfig))

    def test_name(self):
        if self.EXPECTED_NAME and self.APP_CONFIG_CLASS is not None:
            self.assertEqual(self.app_config_class.name, self.expected_name)
