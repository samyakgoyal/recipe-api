from django.test import SimpleTestCase

from app import calc


class CaclTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        res = calc.subtract(15, 6)
        self.assertEqual(res, 9)
