from django.db import models

from edmontonpy.core.models.dals import (
    MeetupDAL, PresentationDAL, PresenterDAL, SponsorDAL)
from edmontonpy.core.models.managers import MeetupManager
from edmontonpy.tests.test_dals import DALTest


class TestMeetupDAL(DALTest):
    DAL_CLASS = MeetupDAL
    PROPERTY_MAP = (
        ('date_time', models.DateTimeField),
        ('sponsor', models.ForeignKey),
        ('url', models.URLField),
    )

    def test_next_meetup(self):
        manager = self.DAL_CLASS._meta.managers_map['objects']
        self.assertIsInstance(manager, MeetupManager)


class TestPresentationDAL(DALTest):
    DAL_CLASS = PresentationDAL
    PROPERTY_MAP = (
        ('name', models.CharField),
        ('presenter', models.ForeignKey),
        ('meetup', models.ForeignKey),
    )


class TestPresenterDAL(DALTest):
    DAL_CLASS = PresenterDAL
    PROPERTY_MAP = (
        ('first_name', models.CharField),
        ('last_name', models.CharField),
        ('email_address', models.EmailField),
        ('github_username', models.CharField),
        ('linkedin_url', models.URLField),
        ('slack_members_id', models.CharField),
        ('twitter_username', models.CharField),
    )


class TestSponsorDAL(DALTest):
    DAL_CLASS = SponsorDAL
    PROPERTY_MAP = (
        ('name', models.CharField),
        ('website_url', models.URLField),
    )
