from tame_of_thrones.Kingdom import Kingdom
import unittest


class TestKingdom(unittest.TestCase):
    def setUp(self):
        self.test_dict = {
            "AIR": {"R": 1, "Z": 1, "O": 1},
            "FIRE": {"J": 1, "X": 1, "G": 1, "M": 1, "U": 1, "T": 1},
            "ICE": {"T": 3, "H": 1, "V": 1, "A": 1, "O": 1},
            "LAND": {"F": 2, "U": 1, "S": 1, "I": 1},
            "SPACE": {"S": 2, "N": 1, "V": 1, "Y": 1, "P": 1, "H": 1},
            "WATER": {"V": 2, "J": 1, "A": 1, "W": 1, "B": 1, "Z": 1},
        }

    def test_is_correctly_encoded(self):
        kingdom = Kingdom()
        self.assertEqual(kingdom.kingdom_dict, self.test_dict)


if __name__ == "__main__":
    unittest.main()
