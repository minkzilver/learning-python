import unittest
from tests.complexTests import TestComplexNumber

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComplexNumber)
    unittest.TextTestRunner(verbosity=2).run(suite)
