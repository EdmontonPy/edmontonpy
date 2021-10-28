import datetime

from django.db import models
from django.utils import timezone

# Keep showing an already-started meetup as the ‘next’ meetup until this long
# after the meetup start time.
DEFAULT_MEETUP_DURATION = datetime.timedelta(hours=4)

class MeetupManager(models.Manager):
    def __init__(self, *args, now_func=None, **kwargs):
        super().__init__(*args, **kwargs)
        if now_func is None:
            now_func = timezone.now
        self.now_func = now_func

    def next_meetup(self, date_time=None):
        if date_time is None:
            date_time = self.now_func()



        return super().get_queryset().filter(
            date_time__gt=date_time - DEFAULT_MEETUP_DURATION
        ).order_by(
            'date_time'
        )[0:1].get()
