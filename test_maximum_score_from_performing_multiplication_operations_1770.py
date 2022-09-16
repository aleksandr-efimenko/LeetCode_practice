import unittest
import maximum_score_from_performing_multiplication_operations_1770 as mx

class MyCase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pass

    def test_maximumScore(self):
        cases = [
            ([1,2,3], [3,2,1], 14),
            ([-5,-3,-3,-2,7,1], [-10,-5,3,4,6], 102),
            ([0],[-1], 0)
        ]
        for nums, multipliers, output in cases:
            result = mx.maximumScore(nums, multipliers)
            self.assertEqual(output, result)