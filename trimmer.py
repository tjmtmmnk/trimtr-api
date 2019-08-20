from nltk.tokenize import sent_tokenize
from typing import List
import re


def trim(raw_body: str) -> str:
    # sent_tokenizeにかけると改行や空白が消えてしまうので先にフラグを立てておいて後で処理する
    flagged_body = _create_new_line_flag(raw_body)
    flagged_body = _create_white_space_flag(flagged_body)

    sentences = _split_body_to_sentences(flagged_body)

    shaped_body = ""
    for s in sentences:
        sentence = _shape_white_space(s)
        sentence = _shape_new_line(sentence)

        shaped_body += sentence

    return shaped_body


def _create_new_line_flag(body: str) -> str:
    return re.sub(r'(\n{2,})|((\r\n){2,})', "[newline]", body)


def _shape_new_line(sentence: str) -> str:
    # [newline] を \n に置換する前に \n を空白に変換する
    shaped_sentence = _new_line_to_white_space(sentence)

    if re.search(r"\[newline\]", sentence):
        shaped_sentence = shaped_sentence.replace("[newline]", "\n\n")
    else:
        shaped_sentence = shaped_sentence + "\n"

    return shaped_sentence


def _shape_white_space(sentence: str) -> str:
    shaped_sentence = sentence

    # 先頭の空白は消す
    if re.match(r'^\[whitespace\]', sentence):
        shaped_sentence = re.sub(r'^\[whitespace\]', '', sentence)

    shaped_sentence = shaped_sentence.replace("[whitespace]", " ")

    return shaped_sentence


def _new_line_to_white_space(sentence: str) -> str:
    return sentence.replace("\n", " ")


def _create_white_space_flag(body: str) -> str:
    return re.sub(r'( {2,})|((\n|\r\n) {1,})', '[whitespace]', body)


def _split_body_to_sentences(body: str) -> List[str]:
    return sent_tokenize(body)
