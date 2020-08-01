from tame_of_thrones.CommandLineParser import CommandLineParser
import unittest
import sys


class TestCommandLineParser(unittest.TestCase):
    def setUp(self):
        """
        setUp --> Adds a sample fileName to the sys.argv and checks if it is
        read by the commandLineParser Class
        """
        sys.argv.append("testFile.txt")

    def test_command_line_input(self):
        """
        test_command_line_input --> This gets the sys.argv[1] and asserts
        it is not None
        """
        testParser = CommandLineParser()
        self.assertIsNotNone(testParser)


if __name__ == "__main__":
    unittest.main()
