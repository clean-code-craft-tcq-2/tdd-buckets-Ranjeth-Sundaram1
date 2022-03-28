import unittest
import examine_samples_A2D_12Bit

class TypewiseTest(unittest.TestCase):
    def test_IgnoreInvalidSamples(self):
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([1122, 2555, 3214, 4094]) == [1122, 2555, 3214, 4094])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([4503, 4094]) == [4094])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([4503]) == [])
        self.assertTrue(examine_samples_A2D_12Bit.IgnoreInvalidSamples([]) == [])
    
    def test_convertA2D_12BIntoAmps(self):
        self.assertTrue(examine_samples_A2D_12Bit.convertA2D_12BIntoAmps([1122, 1800, 3521, 2555, 2022, 3214, 4094]) == [3, 4, 9, 6, 5, 8, 10])
        self.assertTrue(examine_samples_A2D_12Bit.convertA2D_12BIntoAmps([1122, 4095, 3214 ]) == [3, 8])
        self.assertTrue(examine_samples_A2D_12Bit.convertA2D_12BIntoAmps([]) == [])

unittest.main(),
