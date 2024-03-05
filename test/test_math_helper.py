from unittest import TestCase


class Test(TestCase):
    def test_horner_value(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"
        self.assertTrue('FO'.isupper())
