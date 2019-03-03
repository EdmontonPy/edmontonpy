import unittest

from django.db import models


class DALTest(unittest.TestCase):
    DAL_CLASS = None
    PROPERTY_MAP = []

    def test_is_django_model(self):
        if self.DAL_CLASS is not None:
            self.assertTrue(issubclass(self.DAL_CLASS, models.Model))

    def test_meta_abstract(self):
        if self.DAL_CLASS is not None:
            self.assertTrue(self.DAL_CLASS._meta.abstract)

    def test_properties(self):
        if self.DAL_CLASS:
            fields = self.DAL_CLASS._meta.fields
            checked_fields = 0

            for field_name, value in self.PROPERTY_MAP:
                for field in fields:
                    if field.name == field_name:
                        self.assertIsInstance(field, value)
                        checked_fields += 1

            self.assertEqual(len(fields), checked_fields)
