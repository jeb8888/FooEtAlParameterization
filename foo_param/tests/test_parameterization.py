import os
import sys
import unittest

#from foo_param.foo_param import FooParameterization

here = os.path.dirname(__file__)
sys.path.append("..")
sys.path.append(os.path.join(here, '../foo_param'))

from foo_param import FooParameterization

class TestFooParameterization(unittest.TestCase):
    def test_calculate_volume(self):
        param = FooParameterization(3)
        param.validate()
        self.assertAlmostEqual(param.calculate_volume(), 113.097, places=3)

    def test_invalid_radius(self):
        param = FooParameterization(-1)
        with self.assertRaises(ValueError):
            param.validate()

if __name__ == "__main__":
    unittest.main()