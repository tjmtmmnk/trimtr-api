from nltk.tokenize import sent_tokenize
from typing import List
import re


def trim(raw_body: str) -> str:
    # sent_tokenizeにかけると改行や空白が消えてしまうので先にフラグを立てておいて後で処理する
    flagged_body = _create_flag(raw_body)

    sentences = _split_body_to_sentences(flagged_body)

    shaped_body = _create_shaped_body(sentences)

    formatted_shaped_body = _format_shaped_body(shaped_body)

    return formatted_shaped_body


def _create_flag(body: str) -> str:
    flagged_body = _create_sentence_block_flag(body)
    flagged_body = _create_white_space_flag(flagged_body)
    flagged_body = _create_colon_flag(flagged_body)
    return flagged_body


def _create_shaped_body(sentences: List[str]) -> str:
    shaped_body = ""
    for s in sentences:
        sentence = _shape_white_space(s)
        sentence = _shape_new_line(sentence)

        shaped_body += sentence

    return shaped_body


def _format_shaped_body(shaped_body: str) -> str:
    formated_body = _format_two_more_lines(shaped_body)
    return formated_body


def _create_sentence_block_flag(body: str) -> str:
    return re.sub(r'(\n|\r\n){2,}', "[SB]", body)


def _create_white_space_flag(body: str) -> str:
    return re.sub(r'( {2,})|((\n|\r\n) +)', '[WS]', body)


def _create_colon_flag(body: str) -> str:
    return re.sub(r'(\w| ):( |\n|\r\n)+', ':[NL]', body)


def _shape_new_line(sentence: str) -> str:
    # [NL] を \n に置換する前に \n を空白に変換する
    shaped_sentence = _new_line_to_white_space(sentence)

    if re.search(r"\[NL\]", sentence):
        shaped_sentence = shaped_sentence.replace("[NL]", "\n")
    elif re.search(r"\[SB\]", sentence):
        shaped_sentence = shaped_sentence.replace("[SB]", "\n\n")
    else:
        shaped_sentence = shaped_sentence + "\n"

    return shaped_sentence


def _shape_white_space(sentence: str) -> str:
    shaped_sentence = sentence

    # 先頭の空白は消す
    if re.match(r'^\[WS\]', sentence):
        shaped_sentence = re.sub(r'^\[WS\]', '', sentence)

    shaped_sentence = shaped_sentence.replace("[WS]", " ")

    return shaped_sentence


# 文中で変な改行が含まれている時に空白に変換する
def _new_line_to_white_space(sentence: str) -> str:
    return re.sub(r'((\n|\r\n)+)|( +(\n|\r\n)+)|((\n|\r\n)+ +)', ' ', sentence)


def _split_body_to_sentences(body: str) -> List[str]:
    return sent_tokenize(body)


# 文末の改行1個と[SB]の改行2個などで改行が3個以上発生する可能性があるのでその場合は2個に抑え込む
def _format_two_more_lines(body: str) -> str:
    return re.sub(r'((\n|\r\n){3,})', "\n\n", body)
