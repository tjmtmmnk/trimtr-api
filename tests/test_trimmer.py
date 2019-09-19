import unittest
import random
from trimtr.trimmer import Trimmer


class TestTrimmer(unittest.TestCase):
    def setUp(self):
        self.trimmer = Trimmer.get_instance()

    # 文と文の間は改行される
    def test_new_line_between_sentences(self):
        original_sentence = "How are you? I am fine thank you."
        expected_sentence = "How are you?\nI am fine thank you."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 省略形が来た時に改行されない
    def test_abbreviation(self):
        abbreviations = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e', 'e.g', 'u.s', 'etc'])
        random_abbreviation = random.sample(abbreviations, 1)[0]
        expected_sentence = random_abbreviation
        trimmed_sentence = self.trimmer.trim(random_abbreviation)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 文中の不要な空白は消される
    def test_shape_unnecessary_white_space(self):
        original_sentence = "I am  fine thank   you."
        expected_sentence = "I am fine thank you."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 文中の不要な改行は消される
    def test_shape_unnecessary_new_line(self):
        original_sentence = "I am fine\n thank you."
        expected_sentence = "I am fine thank you."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 3個以上の改行は2個にフォーマットされる
    def test_format_new_line(self):
        original_sentence = "How are you?\n\n\nI am fine thank you."
        expected_sentence = "How are you?\n\nI am fine thank you."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 1個の改行は維持される
    def test_sentence_block(self):
        original_sentence = "How are you?\n\nI am fine thank you."
        expected_sentence = "How are you?\n\nI am fine thank you."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # コロン+空白が来たら改行される
    def test_colon(self):
        original_sentence = "I like this: "
        expected_sentence = "I like this:\n"
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # コロン+改行が来たら改行される
    def test_colon_not_new_line(self):
        original_sentence = "This is:\n"
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # コロン+英数字が来たら改行されない
    def test_colon_not_new_line(self):
        original_sentence = "This:is"
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 先頭の空白は消される
    def test_shape_head_white_space(self):
        original_sentence = " How are you?"
        expected_sentence = "How are you?"
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 人名のピリオドが含まれる場合
    def test_not_break_one_sentence(self):
        original_sentence = "Punkt knows that the periods in Mr.Smith and Johann S.Bach do not mark sentence boundaries."
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 数字のピリオドが含まれる場合
    def test_number_period(self):
        original_sentence = "For the quarter that ended March 31, Nokia earned $1.9 billion (1.2 euros), up 25% from the same quarter last year but short of an expected $2.3 billion."
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 空文の場合
    def test_empty(self):
        original_sentence = ""
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 単語だけの場合
    def test_simple_word(self):
        original_sentence = "hello"
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    def test_singleton_trimmer(self):
        new_trimmer = Trimmer.get_instance()
        self.assertEqual(id(self.trimmer), id(new_trimmer))

    # 空白無しで文章が連続する場合
    def test_continuing_sentences_without_white_space(self):
        original_sentence = "A clinical study that lacks a comparison (i.e., a control) group.I like it."
        expected_sentence = "A clinical study that lacks a comparison (i.e., a control) group.\nI like it."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 空白無しで文章が連続する場合
    def test_continuing_sentences_without_white_space(self):
        last_words = set([')', '\"', '>', 'p'])
        last_word = random.sample(last_words, 1)[0]
        original_sentence = "A clinical study that lacks a 2.2 comparison (i.e., a control) grou" + last_word + ".I like it."
        expected_sentence = "A clinical study that lacks a 2.2 comparison (i.e., a control) grou" + last_word + ".\nI like it."
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)

    # 2,3点ドットがそのまま表示される
    def test_dot(self):
        original_sentence = "A1,...,A3,..,A4 is array."
        expected_sentence = original_sentence
        trimmed_sentence = self.trimmer.trim(original_sentence)
        self.assertEqual(expected_sentence, trimmed_sentence)


if __name__ == "__main__":
    unittest.main()
