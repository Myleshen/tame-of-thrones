from tame_of_thrones.ReusableScripts import Reusable


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

    def _parse_file_debug(self):
        """
        _parse_file_debug --> Does the same as parseFile(),
        This takes only the File Name, used only for testing purposes
        Where Absolute Path can't be given everytime

        :return: Contents in the File
        :rtype: List
        """
        reuse_script = Reusable()
        # In Debug the input is only the file name so need to append the path
        debug_file_path = reuse_script.change_name_to_abs_path(
            self.abs_path
        )
        with open(debug_file_path, "r") as input_file:
            for line in input_file.readlines():
                self.file_contents.append(line.strip())
        return self.file_contents
