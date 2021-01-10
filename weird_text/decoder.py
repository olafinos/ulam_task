import re

ENCODER_TOKEN = re.compile(r"\n-weird-\n(.*)\n-weird-\n(.*)", flags=re.DOTALL)
WORD_TOKEN = re.compile(r"(\w+)", re.U)


class WeirdTextDecoder:
    """
    Class for decoding text encoded by WeirdTextEncoder.
    It decodes applying WeirdText rules to given encoded text and original words.
    If given input doesn't match the WeirdText pattern it raises error.
    """

    def __init__(self, encoded_input):

        re_match = ENCODER_TOKEN.match(encoded_input)
        if not re_match:
            raise ValueError("Input does not match the WeirdText pattern")

        self.encoded_text = re_match.group(1)
        self.original_words = WORD_TOKEN.findall(re_match.group(2))
        self.shuffled_words = WORD_TOKEN.findall(self.encoded_text)

    def decode(self) -> str:
        """
        Create decoded text.
        :return: Decoded input text.
        """
        decoded_text = self.encoded_text
        for word in self.shuffled_words:
            decoded_word = self._decode_word(word)
            decoded_text = re.sub(word, decoded_word, decoded_text)
        return decoded_text

    def _decode_word(self, word: str) -> str:
        """
        Decodes given word.
        :param word: Word from encoded input text.
        :return: Decoded word if possible.
        """
        if len(word) <= 3 or len(set(word[1:-1])) == 1:
            return word
        possible_words = filter(
            lambda original_word: original_word.startswith(word[0])
            and original_word.endswith(word[-1]),
            self.original_words,
        )
        for possible_word in possible_words:
            if self._check_if_middle_part_equal(possible_word, word):
                return possible_word
        return word

    def _check_if_middle_part_equal(
        self, original_word: str, permutated_word: str
    ) -> bool:
        """
        Checks if middle part of two given words are equal.
        :param original_word: Word from list of original words.
        :param permutated_word: Word from encoded input text.
        """
        return sorted(original_word[1:-1]) == sorted(permutated_word[1:-1])
