import unittest


class ModelTest(unittest.TestCase):
    MODEL_CLASS = None
    SUB_CLASSES = []

    def test_init(self):
        if self.MODEL_CLASS is not None:
            model = self.MODEL_CLASS()
            for sub_class in self.SUB_CLASSES:
                self.assertIsInstance(model, sub_class)
