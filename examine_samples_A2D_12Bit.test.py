import unittest
import examine_samples_A2D_12Bit

class TypewiseTest(unittest.TestCase):
    def test_IgnoreInvalidSamples(self):
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([1122, 2555, 3214, 4094]) == [1122, 2555, 3214, 4094])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([4503, 4094]) == [4094])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([4503]) == [])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([]) == [])
