from pathlib import Path


class FileParser:
    def parse_file(self, file_path_name):
        """
        parse_file --> Generator function that gives a single line
        each time this function is called

        :param: Takes the Input of the file name
        :yields: Single line from the input file
        :rtype: List[Kingdom, message]
        """
        file_contents = list()
        file_check = Path(file_path_name).exists()
        if file_check:
            with open(file_path_name, "r") as input_file:
                for line in input_file.readlines():
                    file_contents.append(line.strip())
            return file_contents
        else:
            raise FileNotFoundError("Given File is not Found")

    def parse_kingdom_file(self, file_path):
        file_contents = dict()
        file_check = Path(file_path).exists()
        if file_check:
            with open(file_path, "r") as input_file:
                for line in input_file.readlines():
                    kingdom, emblem = line.split()
                    file_contents[kingdom] = emblem
            return file_contents
        else:
            raise FileNotFoundError("Given File is not Found")
