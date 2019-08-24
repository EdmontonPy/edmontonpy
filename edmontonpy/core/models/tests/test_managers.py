import unittest

from datetime import datetime
from unittest.mock import MagicMock, patch

from django.utils import timezone
from pytz import utc

from edmontonpy.core.models.managers import MeetupManager


class TestMeetupManager(unittest.TestCase):
    def setUp(self):
        # When USE_TZ is set, timezone.now is in UTC
        self.date_time = datetime(2018, 12, 29, 22, 30, 15, 400000, tzinfo=utc)
        self.now_func = MagicMock(spec=timezone.now)
        self.now_func.return_value = self.date_time
        self.manager = MeetupManager(
            now_func=self.now_func
        )

    def test_init(self):
        manager = MeetupManager()
        self.assertIsInstance(manager, MeetupManager)
        self.assertEqual(manager.now_func, timezone.now)

    @patch('django.db.models.Manager.get_queryset')
    def _next_meetup_test(self, base_class, **kwargs):
        base_class.return_value = base_class
        base_class.filter.return_value = base_class
        base_class.order_by.return_value = base_class
        base_class.__getitem__.return_value = base_class
        base_class.get.return_value = base_class
        queryset = self.manager.next_meetup(**kwargs)
        base_class.filter.assert_called_once_with(date_time__gt=self.date_time)
        base_class.order_by.assert_called_once_with('date_time')
        base_class.__getitem__.assert_called_once_with(slice(0, 1, None))
        self.assertEqual(queryset, base_class)

    def test_next_meetup(self):
        self._next_meetup_test()

    def test_next_meetup_date_time(self):
        self._next_meetup_test(date_time=self.date_time)
