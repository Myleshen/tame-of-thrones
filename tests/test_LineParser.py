from tame_of_thrones.LineParser import LineParser
import unittest


class TestLineParser(unittest.TestCase):
    def setUp(self):
        self.line_parser = LineParser().parse_line

    def test_correct_line(self):
        line = "AIR ROZO"
        kingdom, message = self.line_parser(line)
        self.assertEqual([kingdom, message], ["AIR", "ROZO"])

    def test_message_seperated_with_spcae(self):
        line = "WATER SUMMER IS COMING"
        kingdom, message = self.line_parser(line)
        self.assertEqual([kingdom, message], ["WATER", "SUMMERISCOMING"])

    def test_no_lines_in_file(self):
        line = ""
        kingdom, message = self.line_parser(line)
        self.assertEqual([kingdom, message], [None, None])

    def test_blank_spaces_in_line(self):
        line = []
        kingdom, message = self.line_parser(line)
        self.assertEqual([kingdom, message], [None, None])


if __name__ == "__main__":
    unittest.main()
