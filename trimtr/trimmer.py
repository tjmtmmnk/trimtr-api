from typing import List
import re
import os
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters


# マルチスレッドにするならスレッドセーフにするためのロック処理が必要そう
# いまはgunicornでマルチプロセスでメモリを共有していないので考えなくて良さそう？
class SentenceTokenizer:
    _unique_instance = None

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        directory = os.path.dirname(os.path.abspath(__file__)) + "/"
        with open(directory + "news.txt", 'r') as f:
            text = f.read()
            return PunktSentenceTokenizer(train_text=text)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()

        return cls._unique_instance


# Trimmerは状態を持たないのでシングルトンにしても問題ないはず
class Trimmer:
    _unique_instance = None

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()

        return cls._unique_instance

    @classmethod
    def trim(cls, raw_body: str) -> str:
        if raw_body == "":
            return ""

        # sent_tokenizeにかけると改行や空白が消えてしまうので先にフラグを立てておいて後で処理する
        flagged_body = cls._create_flag(raw_body)

        sentences = cls._split_body_to_sentences(flagged_body)

        shaped_body = cls._create_shaped_body(sentences)

        formatted_shaped_body = cls._format_shaped_body(shaped_body)

        return formatted_shaped_body

    @classmethod
    def _create_flag(cls, body: str) -> str:
        flagged_body = cls._create_sentence_block_flag(body)
        flagged_body = cls._create_white_space_flag(flagged_body)
        flagged_body = cls._create_colon_flag(flagged_body)
        flagged_body = cls._create_dot_flag(flagged_body)

        # 文章が空白などなしに連続すると文末判定されないので空白を挿入する
        flagged_body = cls._insert_after_period(flagged_body)
        return flagged_body

    @classmethod
    def _create_shaped_body(cls, sentences: List[str]) -> str:
        shaped_body = ""
        for s in sentences:
            sentence = cls._shape_white_space(s)
            sentence = cls._shape_new_line(sentence)
            sentence = cls._shape_dot(sentence)
            shaped_body += sentence

        return shaped_body

    @classmethod
    def _shape_new_line(cls, sentence: str) -> str:
        # [NL] を \n に置換する前に \n を空白に変換する
        shaped_sentence = cls._new_line_to_white_space(sentence)
        is_flag_nl = True if re.search(r"\[NL\]", sentence) else False
        is_flag_sb = True if re.search(r"\[SB\]", sentence) else False
        is_flag_eos = True if re.search(r"\[EOS\]", sentence) else False

        if is_flag_nl:
            shaped_sentence = shaped_sentence.replace("[NL]", "\n")
        if is_flag_sb:
            shaped_sentence = shaped_sentence.replace("[SB]", "\n\n")
        if is_flag_eos:
            shaped_sentence = shaped_sentence.replace("[EOS]", "")

        if not is_flag_nl and not is_flag_sb and not is_flag_eos:
            shaped_sentence = shaped_sentence + "\n"

        return shaped_sentence

    @classmethod
    def _format_shaped_body(cls, shaped_body: str) -> str:
        formatted_body = cls._format_two_more_lines(shaped_body)
        formatted_body = cls._format_white_space_after_period(formatted_body)
        return formatted_body

    @staticmethod
    def _insert_after_period(body: str) -> str:
        return re.sub(r'(\D)\.(\D)', r'\1. \2', body)

    @staticmethod
    def _create_sentence_block_flag(body: str) -> str:
        return re.sub(r'(\n|\r\n){2,}', "[SB]", body)

    @staticmethod
    def _create_white_space_flag(body: str) -> str:
        return re.sub(r'( {2,})|((\n|\r\n) +)', '[WS]', body)

    @staticmethod
    def _create_colon_flag(body: str) -> str:
        return re.sub(r':( |\n|\r\n)+', ':[NL]', body)

    @staticmethod
    def _create_dot_flag(body: str) -> str:
        two_or_three_dot_flag = re.sub(r'\. ?\. ?\.', "[THD]", body)
        two_or_three_dot_flag = re.sub(r'\. ?\.', "[TOD]", two_or_three_dot_flag)
        return two_or_three_dot_flag

    @staticmethod
    def _shape_white_space(sentence: str) -> str:
        shaped_sentence = sentence

        # 先頭の空白は消す
        if re.match(r'^(\[WS\]| +)', sentence):
            shaped_sentence = re.sub(r'^(\[WS\]| +)', '', sentence)

        shaped_sentence = shaped_sentence.replace("[WS]", " ")

        return shaped_sentence

    @staticmethod
    def _shape_dot(sentence: str) -> str:
        shaped_sentence = sentence.replace("[TOD]", "..")
        shaped_sentence = shaped_sentence.replace("[THD]", "...")
        return shaped_sentence

    # 文中で変な改行が含まれている時に空白に変換する
    @staticmethod
    def _new_line_to_white_space(sentence: str) -> str:
        return re.sub(r'((\n|\r\n)+)|( +(\n|\r\n)+)|((\n|\r\n)+ +)', ' ', sentence)

    @staticmethod
    def _split_body_to_sentences(body: str) -> List[str]:
        sent_tokenize = SentenceTokenizer.get_instance()
        sentences = sent_tokenize.tokenize(body)
        sentences[-1] = sentences[-1] + "[EOS]"

        return sentences

    @staticmethod
    # 文末の改行1個と[SB]の改行2個などで改行が3個以上発生する可能性があるのでその場合は2個に抑え込む
    def _format_two_more_lines(body: str) -> str:
        return re.sub(r'((\n|\r\n){3,})', "\n\n", body)

    @staticmethod
    def _format_white_space_after_period(body: str) -> str:
        return re.sub(r'\. ', ".", body)
