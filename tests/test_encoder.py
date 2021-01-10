from unittest import TestCase
from ..encoder import WeirdTextEncoder

INPUT_TEXT = "‘This is a long looong test sentence,\n’‘with some big (biiiiig) words!’"
class TestWeirdTextEncoder(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_text = INPUT_TEXT
        cls.encoder = WeirdTextEncoder(cls.input_text)

    def test_get_all_words_from_text(self):
        expected = ['This', 'is', 'a', 'long', 'looong', 'test', 'sentence', 'with', 'some', 'big', 'biiiiig', 'words']
        self.assertEqual(self.encoder.words, expected)