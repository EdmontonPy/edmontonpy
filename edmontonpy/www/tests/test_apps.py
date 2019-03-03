from edmontonpy.tests.test_apps import AppConfigTest
from edmontonpy.www.apps import WwwConfig


class TestWwwConfig(AppConfigTest):
    EXPECTED_NAME = 'www'
    APP_CONFIG_CLASS = WwwConfig
