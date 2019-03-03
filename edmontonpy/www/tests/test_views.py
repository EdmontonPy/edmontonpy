import unittest

from unittest.mock import MagicMock

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from edmontonpy.core.models import Meetup, Sponsor
from edmontonpy.www.views import IndexTemplateView


class TestIndexTemplateView(unittest.TestCase):
    def setUp(self):
        self.meetup = Meetup()
        self.meetup_class = MagicMock(spec=Meetup)
        self.meetup_class.objects.next_meetup.return_value = self.meetup
        self.sponsors = [Sponsor()]
        self.sponsor_class = MagicMock(spec=Sponsor)
        self.sponsor_class.objects.all.return_value = self.sponsors
        self.view = IndexTemplateView(
            meetup_class=self.meetup_class,
            sponsor_class=self.sponsor_class,
        )
        self.template_name = 'index.html'

    def test_init(self):
        view = IndexTemplateView()
        self.assertIsInstance(view, TemplateView)
        self.assertEqual(view.template_name, self.template_name)
        self.assertEqual(view.meetup_class, Meetup)
        self.assertEqual(view.sponsor_class, Sponsor)

    def test_get_context_data(self):
        context_data = self.view.get_context_data()
        self.assertEqual(context_data['object'], self.meetup)
        self.assertEqual(context_data['sponsors'], self.sponsors)

    def test_get_context_data_meetup_not_found(self):
        self.meetup_class.objects.next_meetup.side_effect = ObjectDoesNotExist
        context_data = self.view.get_context_data()
        self.assertIsNone(context_data['object'])
