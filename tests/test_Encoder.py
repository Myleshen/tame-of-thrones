from tame_of_thrones.Encoder import Encoder
import unittest


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder().encoded_letter_freq
        self.test_dict = {
            "OWL": {"R": 1, "Z": 1, "O": 1},
            "DRAGON": {"J": 1, "X": 1, "G": 1, "M": 1, "U": 1, "T": 1},
            "MAMMOTH": {"T": 3, "H": 1, "V": 1, "A": 1, "O": 1},
            "panda": {"F": 2, "U": 1, "S": 1, "I": 1},
            "gorilla": {"S": 2, "N": 1, "V": 1, "Y": 1, "P": 1, "H": 1},
            "octopus": {"V": 2, "J": 1, "A": 1, "W": 1, "B": 1, "Z": 1},
        }

    def test_does_encoding_work_with_any_case_alphabets(self):
        for key, value in self.test_dict.items():
            self.assertEqual(self.encoder(key), value)
