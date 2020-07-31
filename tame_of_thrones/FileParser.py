class FileParser:
    def __init__(self, file_path_name):
        """
        Takes a single constructor parameter

        :param file_path_name --> Absolute Path to the File
        """
        self.abs_path = file_path_name
        self.file_contents = []

    def parse_file(self):
        """
        parse_file --> Takes abs_path from the current Obj and reads the file

        :return: Contents in the Input File
        :rtype: List
        """
        with open(self.abs_path, "r") as input_file:
            for line in input_file.readlines():
                self.file_contents.append(line.strip())
        return self.file_contents
