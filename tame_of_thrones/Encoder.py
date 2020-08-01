import collections


class Encoder:
    def encoded_letter_freq(self, word, cipher_key=None):
        """
        encoded_letter_freq ---> Encodes any word to the
        length of the word

        The logic used here is that we need to have all the letters
        of the encoded emblem and then the emblem is encoded using the
        length of the emblem.

        :param word: Any Word (Capital Letters Only)
        :type word: String
        :return: Letter_freq_dict after encoding the word
        # Word --> OWL
        # After Encoding --> RZO
        :rtype: Dict
        """
        # Just incase the word is in smaller case
        word = word.upper()
        ceaser_cipher_key = len(word) if cipher_key is None else cipher_key
        encoded_letters = self.__encode_word(word, ceaser_cipher_key)

        return self.__count_letters(encoded_letters)

    def __count_letters(self, letter_array):
        """
        __count_letters counts the freq of each letter
        in letter_array

        :param letter_array: letter_array
        :type letter_array: List
        :return: Freq of each letter in letter_array
        :rtype: Dict{letter: freq}
        """
        return collections.Counter(letter_array)

    def __encode_word(self, word_to_encode, ceaser_cipher_key):
        """
        encode_word Encode the word_to_encode by using the
        ceaser_cipher_key

        :param word_to_encode: Contains the word that is to be encoded
        (The Emblem in this case)
        :type word_to_encode: String
        :param ceaser_cipher_key: Contains the key that is used to encode
        the word_to_encode
        :type ceaser_cipher_key: integer (Number)
        :return: encoded_letters
        :rtype: list of encoded letters
        """
        encoded_letters = list()
        for letter in word_to_encode:
            if ord(letter) - ord("A") + ceaser_cipher_key >= 26:
                encoded_letters.append(
                    chr(ord(letter) - 26 + ceaser_cipher_key)
                )
            else:
                encoded_letters.append(
                    chr(ord(letter) + ceaser_cipher_key)
                )
        return encoded_letters
