from datetime import datetime

import pytz

from edmontonpy.core.models.dals import (
    MeetupDAL, PresentationDAL, PresenterDAL, SponsorDAL)
from edmontonpy.core.models.objects import (
    Meetup, Presentation, Presenter, Sponsor)
from edmontonpy.tests.test_objects import ModelTest


class TestMeetup(ModelTest):
    MODEL_CLASS = Meetup
    SUB_CLASSES = (MeetupDAL, )

    def setUp(self):
        self.date_time = datetime(2018, 12, 29, 22, 30, 15, 400000,
                                  tzinfo=pytz.timezone('America/Edmonton'))
        self.model = self.MODEL_CLASS(
            date_time=self.date_time,
            url='',
        )

    def test_is_virtual_false(self):
        self.assertFalse(self.model.is_virtual)

    def test_is_virtual_true(self):
        self.model.url = 'http://edmontonpy.com/'
        self.assertTrue(self.model.is_virtual)

    def test_str(self):
        self.assertEqual(
            str(self.model),
            str.strip(f'{self.date_time}')
        )


class TestPresentation(ModelTest):
    MODEL_CLASS = Presentation
    SUB_CLASSES = (PresentationDAL, )

    def setUp(self):
        self.first_name = ''
        self.last_name = ''
        self.presenter = Presenter(
            first_name=self.first_name,
            last_name=self.last_name
        )
        self.name = ''
        self.model = self.MODEL_CLASS(
            name=self.name,
            presenter=self.presenter
        )

    def test_str(self):
        self.assertEqual(
            str(self.model),
            f'{self.name} - {self.presenter}'
        )


class TestPresenter(ModelTest):
    MODEL_CLASS = Presenter
    SUB_CLASSES = (PresenterDAL, )

    def setUp(self):
        self.first_name = ''
        self.last_name = ''
        self.model = self.MODEL_CLASS(
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_full_name(self):
        self.assertEqual(
            self.model.full_name,
            str.strip(f'{self.first_name} {self.last_name}')
        )

    def test_str(self):
        self.assertEqual(
            str(self.model),
            str.strip(f'{self.first_name} {self.last_name}')
        )


class TestSponsor(ModelTest):
    MODEL_CLASS = Sponsor
    SUB_CLASSES = (SponsorDAL, )

    def setUp(self):
        self.name = ''
        self.model = self.MODEL_CLASS(
            name=self.name
        )

    def test_str(self):
        self.assertEqual(str(self.model), self.name)
