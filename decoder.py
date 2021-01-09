import re

ENCODER_TOKEN = re.compile(r"\n-weird-\n(.*)\n-weird-\n(.*)", flags=re.DOTALL)
WORD_TOKEN = re.compile(r"(\w+)", re.U)
class WeirdTextDecoder():
    def __init__(self,encoded_input):
        re_match = ENCODER_TOKEN.match(encoded_input)
        if not re_match:
            raise ValueError("Trini")

        self.encoded_text = re_match.group(1)
        self.original_words = WORD_TOKEN.findall(re_match.group(2))
        self.shuffled_words = WORD_TOKEN.findall(self.encoded_text)


