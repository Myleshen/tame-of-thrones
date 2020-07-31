from tame_of_thrones.FileParser import FileParser
import sys


class CommandLineParser:
    def __init__(self):
        """
        __init__ --> Gets the filePath from Command Line.

        """
        self.file_name = sys.argv[1]
        self.file_parser = FileParser(self.file_name)

    def get_file_contents(self):
        """
        get_file_contents --> Uses an instance of FileParser Class,
        to get the File's content

        :return: Contents of the File
        :rtype: List
        """
        return self.file_parser.parse_file()
