from unittest import TestCase
from unittest.mock import patch
from weird_text.encoder import WeirdTextEncoder
from random import Random


class TestWeirdTextEncoder(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_text = "‘This is a long looong test sentence,\n’‘with some big (biiiiig) words!’"
        cls.random = Random(42)
        cls.encoder = WeirdTextEncoder(cls.input_text)

    def test_get_all_words_from_text(self):
        expected = ['This', 'is', 'a', 'long', 'looong', 'test', 'sentence', 'with', 'some', 'big', 'biiiiig', 'words']
        self.assertEqual(self.encoder.words, expected)

    @patch('weird_text.encoder.random')
    def test_encode_word(self, random_choice_mock):
        random_choice_mock.choice._mock_side_effect = self.random.choice
        encoded_word = self.encoder._encode_word('word')
        self.assertEqual(encoded_word, 'wrod')

