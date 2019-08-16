from nltk.tokenize import sent_tokenize
from typing import List
import re


def trim(raw_body: str) -> str:
    new_line_shape = re.sub(r'(\n{2,})|((\r\n){2,})', "[newline]", raw_body)
    white_space_shape = re.sub(r'( {2,})|((\n|\r\n) {1,})', '[whitespace]', new_line_shape)

    token_list = _shape_end_of_sentence(white_space_shape)
    ret = ""
    for t in token_list:
        trimmed_sentence = t

        # 先頭から見たいのでmatchを使う
        if re.match(r'^\[whitespace\]', t):
            trimmed_sentence = re.sub(r'^\[whitespace\]', '', t)

        trimmed_sentence = trimmed_sentence.replace("[newline]", "\n")
        trimmed_sentence = trimmed_sentence.replace("[whitespace]", " ")

        ret += trimmed_sentence + "\n"

    return ret


def _shape_end_of_sentence(body: str) -> List[str]:
    return sent_tokenize(body)
