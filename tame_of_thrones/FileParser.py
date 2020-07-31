class FileParser:
    def parse_file(self, file_path_name):
        """
        parse_file --> Parses the file and returns the contents

        :param: Takes the Input of the file name
        :return: Contents in the Input File
        :rtype: List
        """
        file_contents = list()

        with open(file_path_name, "r") as input_file:
            for line in input_file.readlines():
                file_contents.append(line.strip())
        return file_contents
