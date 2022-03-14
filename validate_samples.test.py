import unittest
import validate_samples

class TypewiseTest(unittest.TestCase):
    def test_PrintSampleDetailsIntoConsole(self):
        self.assertTrue(validate_samples.PrintSampleDetailsIntoConsole([3, 4, 5], 3) == '3-5, 3')

    def test_CountAndPrintSamplesinOneRange(self):
        self.assertTrue(validate_samples.CountAndPrintSamplesinOneRange([3, 4, 5]) == (3, "3-5, 3"))
    
    def test_SplitSamplesInToRanges(self):
        self.assertTrue(validate_samples.SplitSamplesInToRanges([3, 4, 5])==[[3, 4, 5]])
        
    def test_IsSampleHasContinuity(self):
        self.assertTrue(validate_samples.IsSampleHasContinuity(4, [3]) == True)
        self.assertTrue(validate_samples.IsSampleHasContinuity(5, [3]) == False)
        self.assertTrue(validate_samples.IsSampleHasContinuity(5, []) == True)
        self.assertTrue(validate_samples.IsSampleHasContinuity(3, [3]) == True)

    def test_validateSamplesInAllRange(self):
        self.assertTrue(validate_samples.validateSamplesInAllRange([3, 4, 5])==[(3, "3-5, 3")])
        self.assertTrue(validate_samples.validateSamplesInAllRange([2, 3, 4, 5, 7, 9, 10, 12])==[(4, "2-5, 4"), (2, "9-10, 2")])
        self.assertTrue(validate_samples.validateSamplesInAllRange([2, 5, 9])==[])
        
    def test_RemoveOccuranceOneSample(self):
        self.assertTrue(validate_samples.RemoveOccuranceOneSample([[2], [4,5,6], [9],[12,13, 14]]) == [[4,5,6], [12, 13, 14]])
        self.assertTrue(validate_samples.RemoveOccuranceOneSample([[3, 4, 5], [8, 9, 10]]) == [[3, 4, 5], [8, 9, 10]])
        self.assertTrue(validate_samples.RemoveOccuranceOneSample([[2], [4]]) == [])
        self.assertTrue(validate_samples.RemoveOccuranceOneSample([[2], []]) == [])

    def test_RearrangeSamples(self):
        self.assertTrue(validate_samples.RearrangeSamples([1, 4, 2, 7, 5, 8, 9]) == [1, 2, 4, 5, 7, 8, 9])
        self.assertTrue(validate_samples.RearrangeSamples([5, 6, 7]) == [5, 6, 7])
        self.assertTrue(validate_samples.RearrangeSamples([]) == [])

if __name__ == '__main__':
  unittest.main()
