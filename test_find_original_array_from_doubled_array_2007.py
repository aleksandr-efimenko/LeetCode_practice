import unittest
import find_original_array_from_doubled_array_2007 as fo

class FOA_Case(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pass

    def test_findOriginalArray(self):
        cases = [
            ([1,3,4,2,6,8], [1,3,4]),
            ([0,0,0,0], [0,0]),
            ([6,3,0,1], []),
            ([1],[])
        ]
        for input, expected in cases:
            expected.sort()
            result = sorted(fo.findOriginalArray(input))
            self.assertListEqual(expected, result)
