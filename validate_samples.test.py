import unittest
import validate_samples

class TypewiseTest(unittest.TestCase):
    def test_print_sampleRanges_with_count(self):
        self.assertTrue(validate_samples.split_sampleRanges([4,5], 2) == '4-5, 2')


if __name__ == '__main__':
  unittest.main()
