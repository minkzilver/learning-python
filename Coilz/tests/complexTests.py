import unittest
from src.Complex import Complex


class TestComplexNumber(unittest.TestCase):

    def test_realpart(self):
        r = 1.3
        c = Complex(r, 0)
        self.assertEqual(c.r, r)

    def test_imagpart(self):
        i = 1.7
        c = Complex(0, i)
        self.assertEqual(c.i, i)
