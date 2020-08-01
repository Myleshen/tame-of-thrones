from tame_of_thrones.Encoder import Encoder
import collections


class Solver:
    def __init__(self):
        """
        __init__ --> Initializes the kingdom dict which has the kingdom name as
        key and emblem, length of emblem as a list
        Initializes a list for the instance to save all the regions that
        formed the pact with SPACE region
        """
        self.kingdom_dict = {
            "AIR": "OWL",
            "FIRE": "DRAGON",
            "ICE": "MAMMOTH",
            "LAND": "PANDA",
            "SPACE": "GORILLA",
            "WATER": "OCTOPUS",
        }
        self.kingdoms_pact_forged_with = list()
        self.encoder = Encoder()

    def __check_if_won_over_kingdom(self, to_kingdom, encoded_string):
        """
        __check_if_won_over_kingdom --> Checks if the encoded string
        has the required letters.

        :param to_kingdom: Kingdom Name
        :type to_kingdom: String
        :param encoded_string: Secret Message sent by Land Ruler
        :type encoded_string: String
        :return: True / False
        based on whether the kingdom accepted the alligance
        :rtype: Boolean
        """
        freq_dict_encoded_letter = self.encoder.encoded_letter_freq(
            self.kingdom_dict[to_kingdom], encoded_string,
        )
        # Just incase if there are any small letter by any mistake
        encoded_string = encoded_string.upper()
        encoded_string_counter = collections.Counter(encoded_string)
        for key, value in freq_dict_encoded_letter.items():
            if encoded_string_counter[key] < freq_dict_encoded_letter[key]:
                return False
        return True

    def if_accepted_add_to_forged_pact_list(
        self, to_kingdom, encoded_string
    ):
        """
        if_accepted_add_to_forged_pact_list --> Adds the kingdom to object's
        internal variable named kingdoms_pact_forged_with.

        :param to_kingdom: Contains the Kingdom Name
        :type to_kingdom: String
        :param encoded_string: Contains the encoded_string
        :type encoded_string: String
        """
        if self.__check_if_won_over_kingdom(to_kingdom, encoded_string):
            if to_kingdom not in self.kingdoms_pact_forged_with:
                self.kingdoms_pact_forged_with.append(to_kingdom)

    def print_answer(self):
        """
        print_answer --> Prints the final answer based on the required output
        """
        if len(self.kingdoms_pact_forged_with) >= 3:
            print(*["SPACE", *self.kingdoms_pact_forged_with])
        else:
            print("NONE")
