import unittest
import examine_samples

class TypewiseTest(unittest.TestCase):
    def test_PrintSampleDetailsIntoConsole(self):
        self.assertTrue(examine_samples.PrintSampleDetailsIntoConsole([3, 4, 5], 3) == '3-5, 3')
        self.assertTrue(examine_samples.PrintSampleDetailsIntoConsole([1, 1, 2, 3], 4) == '1-3, 4')

    def test_CountAndPrintSamplesinOneRange(self):
        self.assertTrue(examine_samples.CountSamplesinOneRange([3, 4, 5]) == (3, "3-5, 3"))
        self.assertTrue(examine_samples.CountSamplesinOneRange([1, 1, 2, 3]) == (4,'1-3, 4'))
        self.assertTrue(examine_samples.CountSamplesinOneRange([]) == (0, "No data to print"))

    def test_IsSampleHasContinuity(self):
        self.assertTrue(examine_samples.IsSampleHasContinuity(4, [3]) == True)
        self.assertTrue(examine_samples.IsSampleHasContinuity(5, [3]) == False)
        self.assertTrue(examine_samples.IsSampleHasContinuity(5, []) == True)
        self.assertTrue(examine_samples.IsSampleHasContinuity(3, [3]) == True)

    def test_SplitSamplesInToRanges(self):
        self.assertTrue(examine_samples.SplitSamplesInToRanges([3, 4, 5])==[[3, 4, 5]])
        self.assertTrue(examine_samples.SplitSamplesInToRanges([1, 2, 2, 4, 5])==[[1, 2, 2], [4, 5]])

    def test_IdentifyRangesofSamples(self):
        self.assertTrue(examine_samples.IdentifyRangesofSamples([3, 4, 5])==[(3, "3-5, 3")])
        self.assertTrue(examine_samples.IdentifyRangesofSamples([2, 3, 4, 5, 7, 9, 10, 12])==[(4, "2-5, 4"), (2, "9-10, 2")])
        self.assertTrue(examine_samples.IdentifyRangesofSamples([2, 5, 9])==[])
        self.assertTrue(examine_samples.IdentifyRangesofSamples([])==[])

    def test_RemoveOccuranceOneSample(self):
        self.assertTrue(examine_samples.RemoveOccuranceOneSample([[2], [4,5,6], [9],[12,13, 14]]) == [[4,5,6], [12, 13, 14]])
        self.assertTrue(examine_samples.RemoveOccuranceOneSample([[3, 4, 5], [8, 9, 10]]) == [[3, 4, 5], [8, 9, 10]])
        self.assertTrue(examine_samples.RemoveOccuranceOneSample([[2], [4]]) == [])
        self.assertTrue(examine_samples.RemoveOccuranceOneSample([[2], []]) == [])

    def test_RearrangeSamples(self):
        self.assertTrue(examine_samples.RearrangeSamples([1, 4, 2, 7, 5, 8, 9]) == [1, 2, 4, 5, 7, 8, 9])
        self.assertTrue(examine_samples.RearrangeSamples([5, 6, 7]) == [5, 6, 7])
        self.assertTrue(examine_samples.RearrangeSamples([]) == [])

unittest.main(),
