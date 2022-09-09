import unittest
import the_number_of_weak_characters_in_the_game_1996 as nw

class MyTest(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.solution = nw.Solution()
        self.properties_list = [
            ([[5, 5], [6, 3], [3, 6]], 0),
            ([[2, 2], [3, 3]], 1),
            ([[1, 5], [10, 4], [4, 3]], 1),
            ([[1, 5], [10, 4], [4, 3], [2, 6], [5, 4], [6, 5]], 3),
            ([[0, 0], [0, 0]], 0),
            ([[1, 1], [2, 1], [2, 2], [1, 2]], 1),
            ([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2)
        ]

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_numberOfWeakCharacters_brute_force(self):
        for properties, expected in self.properties_list:
            result = self.solution.numberOfWeakCharacters(properties)
            self.assertEqual(expected, result)

    def test_numberOfWeakCharacters_improved_brute_force(self):
        for properties, expected in self.properties_list:
            result = self.solution.numberOfWeakCharacters_improved_brute_force(properties)
            self.assertEqual(expected, result)

    def test_numberOfWeakCharacters_two_max(self):
        for properties, expected in self.properties_list:
            result = self.solution.numberOfWeakCharacters_two_max(properties)
            self.assertEqual(expected, result)

    def test_numberOfWeakCharacters(self):
        for properties, expected in self.properties_list:
            result = self.solution.numberOfWeakCharacters(properties)
            self.assertEqual(expected, result)

