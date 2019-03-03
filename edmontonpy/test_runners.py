import os

import django

from unittest.mock import patch

from django.conf import settings
from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from django.test.utils import get_runner


def test_suite():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "edmontonpy.settings"
    )
    django.setup()
    test_runner = get_runner(settings)
    return test_runner().build_suite()


class NoDatabaseTestSuiteRunner(DiscoverRunner):
    """
    NOTE: This code was adapted from the following blog post.
    http://www.caktusgroup.com/blog/2013/10/02/skipping-test-db-creation/
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temp_parallel = self.parallel
        self.parallel = 1

    def build_suite(self, *args, **kwargs):
        """
        Filter TestCases down to unit tests only, removing any
        integration tests.  Since TransactionTestCase requires the
        database, any subclass of it will be considered an integration
        test.

        I.E. Filter tests down to SimpleTestCase, and unittest.TestCase.
        """
        suite = super().build_suite(*args, **kwargs)
        self.parallel = self.temp_parallel

        filtered_suite = self.test_suite()

        for test in suite:
            # TransactionTestCase inherits from SimpleTestCase, and
            # TestCase inherits from TransactionTestCase; so, we filter
            # those 2 out.
            if not isinstance(test, TransactionTestCase):
                filtered_suite.addTest(test)

        if self.parallel > 1:
            parallel_filtered_suite = self.parallel_test_suite(
                filtered_suite,
                self.parallel,
                self.failfast
            )
            parallel_filtered_suite.addTests(filtered_suite)
            filtered_suite = parallel_filtered_suite
        return filtered_suite

    def setup_databases(self, *args, **kwargs):
        self._db_patch = patch('django.db.backends.utils.CursorWrapper')
        db_mock = self._db_patch.start()
        db_mock.side_effect = RuntimeError(
            'No testing the database in unit tests!'
        )
        return None

    def teardown_databases(self, *args, **kwargs):
        self._db_patch.stop()
        return None
