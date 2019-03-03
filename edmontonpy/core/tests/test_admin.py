import unittest

from django.contrib import admin

from edmontonpy.core.models import Meetup, Presentation, Presenter, Sponsor


class TestAdmin(unittest.TestCase):
    MODELS = (
        Meetup,
        Presentation,
        Presenter,
        Sponsor,
    )

    def test_admin(self):
        for model in self.MODELS:
            self.assertTrue(admin.site.is_registered(model))
