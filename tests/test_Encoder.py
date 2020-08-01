from tame_of_thrones.Encoder import Encoder
import unittest


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()
        self.test_dict = {
            "AIR": ["OWL", "RZO"],
            "FIRE": ["DRAGON", "JXGMUT"],
            "ICE": ["MAMMOTH", "THTTVAO"],
            "LAND": ["PANDA", "UFSIF"],
            "SPACE": ["GORILLA", "NVYPSSH"],
            "WATER": ["OCTOPUS", "VJAVWBZ"],
        }

    def test_does_encoding_work(self):
        pass
