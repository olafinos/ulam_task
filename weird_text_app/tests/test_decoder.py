from unittest import TestCase
from ..weird_text.decoder import WeirdTextDecoder


class TestWeirdTextDecoder(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.encoded_text = (
            "\n-weird-\nTihs is a lnog loonog tset scnenete,\nwtih smoe big (biiiiig) wrdos!\n-weird-\n"
            "long looong sentence some test This with words"
        )
        cls.decoder = WeirdTextDecoder(cls.encoded_text)

    def test_shuffled_words_attribute(self):
        expected_words = [
            "Tihs",
            "is",
            "a",
            "lnog",
            "loonog",
            "tset",
            "scnenete",
            "wtih",
            "smoe",
            "big",
            "biiiiig",
            "wrdos",
        ]
        self.assertEqual(self.decoder.shuffled_words, expected_words)

    def test_original_words_attribute(self):
        expected_words = [
            "long",
            "looong",
            "sentence",
            "some",
            "test",
            "This",
            "with",
            "words",
        ]
        self.assertEqual(self.decoder.original_words, expected_words)

    def test_check_if_middle_part_equal(self):
        original_word = "word"
        permuted_word = "wrod"
        self.assertTrue(
            self.decoder._check_if_middle_part_chars_equal(original_word, permuted_word)
        )
        self.assertFalse(
            self.decoder._check_if_middle_part_chars_equal(original_word, "wood")
        )

    def test_decode_word(self):
        word = "loonog"
        expected_word = "looong"
        self.assertEqual(self.decoder._decode_word(word), expected_word)
        self.assertEqual(self.decoder._decode_word("big"), "big")

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            WeirdTextDecoder("WRONG_INPUT")

    def test_decode(self):
        expected_text = (
            "This is a long looong test sentence,\nwith some big (biiiiig) words!"
        )
        self.assertEqual(self.decoder.decode(), expected_text)
