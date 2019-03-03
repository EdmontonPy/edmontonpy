from django.db import models
from django.utils import timezone


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
            date_time__gt=date_time
        ).order_by(
            'date_time'
        )[0:1].get()
