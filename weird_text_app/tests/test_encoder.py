from unittest import TestCase
from unittest.mock import patch
from ..weird_text.encoder import WeirdTextEncoder
from random import Random


class TestWeirdTextEncoder(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_text = (
            "This is a long looong test sentence,\nwith some big (biiiiig) words!"
        )
        cls.random = Random(42)
        cls.encoder = WeirdTextEncoder(cls.input_text)

    def test_get_all_words_from_text(self):
        expected = [
            "This",
            "is",
            "a",
            "long",
            "looong",
            "test",
            "sentence",
            "with",
            "some",
            "big",
            "biiiiig",
            "words",
        ]
        self.assertEqual(self.encoder.words, expected)

    @patch("weird_text_app.weird_text.encoder.random")
    def test_encode_word(self, random_choice_mock):
        random_choice_mock.choice._mock_side_effect = self.random.choice
        encoded_word = self.encoder._encode_word("word")
        expected_word = "wrod"
        self.assertEqual(encoded_word, expected_word)

    @patch("weird_text_app.weird_text.encoder.random")
    def test_encode_text(self, random_choice_mock):
        random_choice_mock.choice._mock_side_effect = self.random.choice
        encoded_text = self.encoder._encode_text()
        expected_text = (
            "Tihs is a lnog loonog tset scenente,\nwtih smoe big (biiiiig) wdros!"
        )
        self.assertEqual(encoded_text, expected_text)

    @patch("weird_text_app.weird_text.encoder.random")
    def test_encode(self, random_choice_mock):
        random_choice_mock.choice._mock_side_effect = self.random.choice
        encoded_text = self.encoder.encode()
        expected_text = (
            "\n-weird-\nTihs is a lnog loonog tset sectenne,\nwtih smoe big (biiiiig) wrods!"
            "\n-weird-\nlong looong sentence some test This with words"
        )
        self.assertEqual(encoded_text, expected_text)

    def test_create_final_output(self):
        output = self.encoder._create_final_output(self.input_text)
        expected_output = (
            "\n-weird-\nThis is a long looong test sentence,\n"
            "with some big (biiiiig) words!\n-weird-\n"
        )
        self.assertEqual(output, expected_output)
