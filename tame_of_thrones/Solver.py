import collections


class Solver:
    def __init__(self):
        """
        __init__ --> Initializes the kingdom dict which has the kingdom name as
        key and emblem, length of emblem as a list
        """
        self.kingdom_dict = {
            "AIR": ["OWL", 3],
            "FIRE": ["DRAGON", 6],
            "ICE": ["MAMMOTH", 7],
            "LAND": ["PANDA", 5],
            "SPACE": ["GORILLA", 7],
            "WATER": ["OCTOPUS", 7],
        }
        self.kingdoms_pact_forged_with = list()

    def __required_letters_to_form_pact(self, to_kingdom):
        """
        __required_letters_to_form_pact ---> Encodes the emblem,
        using the length of the emblem ("OWL" --> 3)

        The logic used here is that we need to have all the letters
        of the encoded emblem and then the emblem is encoded using the
        length of the emblem.

        :param to_kingdom: Kingdom Name (Capital Letters Only)
        :type to_kingdom: String
        :return: Encoded letters that are necessary in the encoded string
        # Emblem --> OWL
        # After Encoding --> RZO
        # The Encoded letters should be \
        present in the encoded string to form the pact
        :rtype: Letters that are required to be present in the encoded string
        """
        emblem, ceaser_cipher_key = self.kingdom_dict[to_kingdom]
        letters_required = list()
        for letter in emblem:
            if ord(letter) - ord("A") + ceaser_cipher_key >= 26:
                letters_required.append(
                    chr(ord(letter) - 26 + ceaser_cipher_key)
                )
            else:
                letters_required.append(
                    chr(ord(letter) + ceaser_cipher_key)
                )

        return letters_required

    def __count_required_letter(self, letters_required):
        """
        __count_required_letter counts the freq of each letter
        in letters_required

        :param letters_required: letters_required
        :type letters_required: List
        :return: Freq of each letter in letters_required
        :rtype: Dict{letter: freq}
        """
        return collections.Counter(letters_required)

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
        letters_needed_to_win_over = self.__required_letters_to_form_pact(
            to_kingdom
        )
        letter_count_dict = self.__count_required_letter(
            letters_needed_to_win_over
        )
        # Just incase if there are any small letter
        encoded_string = encoded_string.upper()
        for letter, freq in letter_count_dict.items():
            if encoded_string.count(letter) < freq:
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
            self.kingdoms_pact_forged_with.append(to_kingdom)

    def print_answer(self):
        """
        print_answer --> Prints the final answer based on the required output
        """
        if len(self.kingdoms_pact_forged_with) >= 3:
            print(*["SPACE", *self.kingdoms_pact_forged_with])
        else:
            print("NONE")
