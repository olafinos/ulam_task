from typing import List
from itertools import permutations
import random
import re


class WeirdTextEncoder:
    """
    Class for Weird Text encoding.

    Permutates every word in a way that first and last character stays at their original place, when every other
    characters is shuffled if possible. Also whitespaces, punctuations, etc. stays at their original places. Encoded
    text is wrapped in a separator. It also adds sorted list of original words to the last line.
    """

    def __init__(self, input_text, separator="\n-weird-\n"):
        self.separator = separator
        self.text = input_text
        self.words = self._get_all_words_from_text()
        self.shuffled_words = []

    def _get_all_words_from_text(self) -> List[str]:
        """
        Separate all words from input text.
        :return: List with input text words
        """
        regex_token = re.compile(r"(\w+)", re.U)
        return regex_token.findall(self.text)

    def encode(self) -> str:
        """
        Encode input text to Weird Text format. Also adds separator between encoded text and sorted shuffled words.
        :return: Encoded input text.
        """
        encoded_text = self._encode_text()
        return self._create_final_output(encoded_text)

    def _encode_text(self) -> str:
        """
        Create encoded text.
        :return: Encoded input text.
        """
        encoded_text = self.text
        for word in self.words:
            encoded_word = self._encode_word(word)
            encoded_text = re.sub(word, encoded_word, encoded_text)
            if encoded_word != word:
                self.shuffled_words.append(word)
        return encoded_text

    def _encode_word(self, word: str) -> str:
        """
        Encodes single word if possible. If its not it returns original word.
        :param word: Word from input text.
        :return: Encoded word if possible.
        """
        if len(word) <= 3 or len(set(word[1:-1])) == 1:
            return word
        else:
            first_letter, last_letter, middle_part = word[0], word[-1], word[1:-1]
            permutation_list = list(permutations(middle_part))
            while permutation_list:
                permutated_middle_part = random.choice(permutation_list)
                permutation_list.remove(permutated_middle_part)
                if permutated_middle_part == tuple(middle_part):
                    continue
                else:
                    break

            return f"{first_letter}{''.join(permutated_middle_part)}{last_letter}"

    def _create_final_output(self, encoded_text: str) -> str:
        """
        Adds separator and sorted shuffled words to encoded text
        :param encoded_text: Encoded text.
        :return: Separated encoded text with sorted shuffled words.
        """
        sorted_shuffled_words = " ".join(sorted(self.shuffled_words, key=str.lower))
        return f"{self.separator}{encoded_text}{self.separator}{sorted_shuffled_words}"
