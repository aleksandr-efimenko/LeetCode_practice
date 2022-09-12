import unittest
import bag_of_tokens_948 as bg

class Bag_of_tokens_testcase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.solution = bg.Solution()

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_bagOfTokensScore(self):
        input_list = [
            ([], 80, 0),
            ([100], 50, 0),
            ([81, 91, 31], 73, 1),
            ([43, 61, 92], 97, 1),
            ([33,4,28,24,96],35, 3),
            ([100, 200], 150, 1),
            ([100, 200, 300, 400], 200, 2)]
        for case in input_list:
            tokens, power, expected = case
            result = self.solution.bagOfTokensScore(tokens=tokens, power=power)
            self.assertEqual(expected, result, msg=case)
