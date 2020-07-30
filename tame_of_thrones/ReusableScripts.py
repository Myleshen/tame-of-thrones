import os


class Reusable:
    def change_name_to_abs_path(self, file_name):
        return "".join([os.getcwd(), "/inputs/", file_name])
