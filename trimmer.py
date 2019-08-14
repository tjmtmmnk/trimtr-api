from tokenizer import Tokenizer
from typing import List


def trim(raw_body):
    token_list = _sharp_end_of_sentence(raw_body)
    for x in token_list:
        print(x)
        print("-" * 20)


def _sharp_end_of_sentence(body: str) -> List[str]:
    tok = Tokenizer.get_instance()
    return tok.tokenize(body)
