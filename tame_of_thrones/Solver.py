import collections


class Solver:
    def __init__(self):
        """
        __init__ --> Initializes a list for the instance to save
        all the regions that formed the pact with SPACE region
        """
        self.kingdoms_pact_forged_with = list()

    def __check_if_won_over_kingdom(
        self, to_kingdom, encoded_string, encoded_emblem_dict
    ):
        """
        __check_if_won_over_kingdom --> Checks if the encoded string
        has the required letters.
        The Encoded emblem letters should be \
        present in the encoded string to form the pact

        :param to_kingdom: Kingdom Name
        :type to_kingdom: String
        :param encoded_string: Secret Message sent by Land Ruler
        :type encoded_string: String
        :param encoded_emblem_dict: Dictionary containing letter freq
        of encoded emblem
        :type encoded_emblem_dict: Dict
        :return: True / False
        based on whether the kingdom accepted the alligance
        :rtype: Boolean
        """
        # Just incase if there are any small letter by any mistake
        encoded_string = encoded_string.upper()

        encoded_string_counter = collections.Counter(encoded_string)
        for key, value in encoded_emblem_dict.items():
            if encoded_string_counter[key] < encoded_emblem_dict[key]:
                return False

        return True

    def if_accepted_add_to_forged_pact_list(
        self, to_kingdom, encoded_string, encoded_emblem_freq
    ):
        """
        if_accepted_add_to_forged_pact_list --> Adds the kingdom to object's
        internal variable named kingdoms_pact_forged_with.
        --> Also checks for redundancy here, this is a redundancy check since
        the main file check's it there itself
        :param to_kingdom: Contains the Kingdom Name
        :type to_kingdom: String
        :param encoded_string: Contains the encoded_string
        :type encoded_string: String
        :param encoded_emblem_freq: Dictionary containing the encoded letter
        frequency
        :type encoded_emblem_freq: Dict
        """
        if (
            self.__check_if_won_over_kingdom(
                to_kingdom, encoded_string, encoded_emblem_freq
            )
            and to_kingdom not in self.kingdoms_pact_forged_with
        ):
            self.kingdoms_pact_forged_with.append(to_kingdom)

    def print_answer(self):
        """
        print_answer --> Prints the final answer based on the required output
        """
        if len(self.kingdoms_pact_forged_with) >= 3:
            print(*["SPACE", *self.kingdoms_pact_forged_with])
        else:
            print("NONE")
