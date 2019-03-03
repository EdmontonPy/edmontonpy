from edmontonpy.core.apps import CoreConfig
from edmontonpy.tests.test_apps import AppConfigTest


class TestWwwConfig(AppConfigTest):
    EXPECTED_NAME = 'core'
    APP_CONFIG_CLASS = CoreConfig
