import unittest
import examine_samples_A2D_10Bit

class TypewiseTest(unittest.TestCase):
    def test_IgnoreInvalidSamples(self):
        self.assertTrue(examine_samples_A2D_10Bit.IgnoreInvalidSamples([-20, 100, 200, 321, 409, 521, 821, 934, 1011, 1024]) == [100, 200, 321, 409, 521, 821, 934, 1011])
        self.assertTrue(examine_samples_A2D_10Bit.IgnoreInvalidSamples([0, 1024, 1055]) == [0])
        self.assertTrue(examine_samples_A2D_10Bit.IgnoreInvalidSamples([1055]) == [])
        self.assertTrue(examine_samples_A2D_10Bit.IgnoreInvalidSamples([]) == [])
    
    def test_convertA2D_10BIntoAmps(self):
        self.assertTrue(examine_samples_A2D_10Bit.convertA2D_10BIntoAmps([-20, 100, 150, 200, 250, 280, 0, 409, 480, 821, 934, 989, 1011, 1024]) == [12, 11, 9, 8, 7, 15, 3, 1, 9, 12, 14, 15])
        self.assertTrue(examine_samples_A2D_10Bit.convertA2D_10BIntoAmps([0, 1022, 1055]) == [15, 15])
        self.assertTrue(examine_samples_A2D_10Bit.convertA2D_10BIntoAmps([1055]) == [])
        self.assertTrue(examine_samples_A2D_10Bit.convertA2D_10BIntoAmps([]) == [])

    def test_ExamineSamplesFrom_A2D(self):
        self.assertTrue(examine_samples_A2D_10Bit.ExamineSamplesFrom_A2D([-20, 100, 150, 200, 250, 280, 0, 409, 480, 821, 934, 989, 1011, 1024]) == [(4, "7-9, 4"), (3, "11-12, 3"),(3, "14-15, 3")])
        self.assertTrue(examine_samples_A2D_10Bit.ExamineSamplesFrom_A2D([200, 409, 1024 ]) == [])
        self.assertTrue(examine_samples_A2D_10Bit.ExamineSamplesFrom_A2D([4100]) == [])
        self.assertTrue(examine_samples_A2D_10Bit.ExamineSamplesFrom_A2D([]) == [])

unittest.main(),
