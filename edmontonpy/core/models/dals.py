from django.db import models

from .managers import MeetupManager


class MeetupDAL(models.Model):
    date_time = models.DateTimeField(unique=True)

    sponsor = models.ForeignKey(
        'Sponsor',
        on_delete=models.PROTECT,
        blank=True
    )
    url = models.URLField(blank=True)

    objects = MeetupManager()

    class Meta:
        abstract = True


class PresentationDAL(models.Model):
    name = models.CharField(max_length=64)
    presenter = models.ForeignKey('Presenter', on_delete=models.PROTECT)

    meetup = models.ForeignKey(
        'Meetup',
        on_delete=models.PROTECT,
        related_name='presentations'
    )

    class Meta:
        abstract = True


class PresenterDAL(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)

    email_address = models.EmailField(blank=True)
    github_username = models.CharField(max_length=64, blank=True)
    linkedin_url = models.URLField(blank=True)
    slack_members_id = models.CharField(max_length=64, blank=True)
    twitter_username = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True


class SponsorDAL(models.Model):
    name = models.CharField(max_length=64)

    website_url = models.URLField(blank=True)

    class Meta:
        abstract = True
