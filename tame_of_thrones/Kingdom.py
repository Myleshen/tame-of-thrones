from tame_of_thrones.FileParser import FileParser
from tame_of_thrones.Encoder import Encoder
import os


class Kingdom:
    def __init__(self):
        """
        __init__ Automatically gets the kingdom data from the input file
        and then encodes the emblems

        self.kingdom_dict = {
            kingdom name: [encoded_emblem, encoded_letter_freq_dict]
            }
        """
        self.file_parser = FileParser()
        self.kingdom_dict = self.__create_encoded_emblems_and_get_letter_freq(
            "".join([os.getcwd(), "/KingdomData.txt"])
        )

    def __generate_kingdom_and_emblem_from_file(self, path_to_file):
        """
        __generate_kingdom_and_emblem_from_file -->  Calls the File Parser
        instance in the constructor and gets the data from it

        :param path_to_file: path of the file is actually hardcoded here
        since we can only take one input argument
        :type path_to_file: string (File path)
        :return: Dict{Kingdom: emblem} # directly read from file
        :rtype: Dict
        """
        return self.file_parser.parse_kingdom_file(path_to_file)

    def __create_encoded_emblems_and_get_letter_freq(self, path_to_file):
        """
        __create_encoded_emblems_and_get_letter_freq --> Gets the data
        from the file and then gives it to the encoder and gets the
        encoded emblem and encode emblem's letter frequency

        :param path_to_file: path of the file (Hardcoded)
        :type path_to_file: string
        :return: Dict{Kingdom: [emblem, letter_freq_dict]}
        :rtype: Dict
        """
        content_dict = self.__generate_kingdom_and_emblem_from_file(
            path_to_file
        )
        return self.__encode_emblem_names(content_dict)

    def __encode_emblem_names(self, kingdom_dict):
        """
        __encode_emblem_names --> Uses the encoder class to
        encode the emblem names and get the letter frequency

        :param kingdom_dict: Dict{Kingdom: emblem}
        :type kingdom_dict: dict
        :return: Dict{Kingdom: [emblem, letter_freq_dict]}
        :rtype: Dict
        """
        encoder = Encoder()
        for key, value in kingdom_dict.items():
            kingdom_dict[key] = encoder.encoded_letter_freq(
                value, len(value)
            )
        return kingdom_dict
