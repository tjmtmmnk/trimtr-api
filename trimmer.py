from nltk.tokenize import sent_tokenize
from typing import List


def trim(raw_body):
    token_list = _sharp_end_of_sentence(raw_body)
    ret = ""
    for t in token_list:
        ret += t + "\n"

    return ret


def _sharp_end_of_sentence(body: str) -> List[str]:
    return sent_tokenize(body)
