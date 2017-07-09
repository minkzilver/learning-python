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

    def test_add(self):
        c1 = Complex(1, 3)
        c2 = Complex(7, 11)

        c3 = c1.add(c2)
        self.assertEqual(c3.r, 8)
        self.assertEqual(c3.i, 14)
