from tame_of_thrones.FileParser import FileParser
import unittest
import os


"""
Since The FileParser class takes only the absolute path.
For Testing Purposes the input files are in the rootDirectory/inputs folder
To automate the loading of files
"""


class TestFileParser(unittest.TestCase):
    def setUp(self):
        """
        setUp Input Directory for tests is the current directory
        + inputs folder This function setsup the file directory
        and gets the file names from it
        """
        self.input_file_directory = "".join([os.getcwd(), "/inputs/"])
        self.input_file_list = os.listdir(self.input_file_directory)

    def test_input_files_are_not_empty(self):
        for file_name in self.input_file_list:
            current_file_path = "".join(
                [self.input_file_directory + "/" + file_name]
            )
            parser_object = FileParser(current_file_path)
            contents = parser_object.parse_file()
            if "failing" in file_name:
                self.assertEqual(contents, [])
            else:
                self.assertIsNotNone(contents)


if __name__ == "__main__":
    unittest.main()
