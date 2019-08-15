from nltk.tokenize import sent_tokenize
from typing import List
import re


def trim(raw_body: str) -> str:
    new_line_shape = re.sub(r'(\n{2,})|((\r\n){2,})', "[newline]", raw_body)

    token_list = _shape_end_of_sentence(new_line_shape)
    ret = ""
    for t in token_list:
        ret += t.replace("[newline]", "\n") + "\n"

    print(ret)
    return ret


def _shape_end_of_sentence(body: str) -> List[str]:
    return sent_tokenize(body)
