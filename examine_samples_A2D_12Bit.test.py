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
    def test_ExamineSamplesFrom_A2D(self):
        self.assertTrue(examine_samples_A2D_12Bit.ExamineSamplesFrom_A2D([1122, 1800, 3521, 2555, 2022, 3214, 4094]) == [(4, "3-6, 4"), (3, "8-10, 3")])
        self.assertTrue(examine_samples_A2D_12Bit.ExamineSamplesFrom_A2D([1122, 4095, 1800, 2022]) == [(3, "3-5, 3")])
        self.assertTrue(examine_samples_A2D_12Bit.ExamineSamplesFrom_A2D([1122, 4095, 3214 ]) == [])
        self.assertTrue(examine_samples_A2D_12Bit.ExamineSamplesFrom_A2D([4100]) == [])
        self.assertTrue(examine_samples_A2D_12Bit.ExamineSamplesFrom_A2D([]) == [])
        
unittest.main(),
