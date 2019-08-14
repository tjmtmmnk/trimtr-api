from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext

from threading import Lock


# 何回も学習させる必要はないのでシングルトンパターンにしておく
class Tokenizer:
    _unique_instance = None
    _lock = Lock()  # クラスロック

    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        text = webtext.raw('overheard.txt')
        return PunktSentenceTokenizer(text)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            with cls._lock:
                if not cls._unique_instance:
                    cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance
