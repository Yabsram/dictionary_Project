import unittest
from unittest.mock import patch
from user_input import get_user_input
class TestGetUserInput(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        "this sentence is bad",  # Invalid
        "try again_",   # Invalid
        "this _ is good.",  # Valid
        "dog", "cat", "q"   # Words
    ])
    def test_sentence_and_words(self, mock_input):
        sentence, words = get_user_input()
        self.assertEqual(sentence, "this _ is good.")
        self.assertEqual(words, ["dog", "cat"])

    @patch('builtins.input', side_effect=[
        "this _ works!", "q"])
    def test_no_words_entered(self, mock_input):
        sentence, words = get_user_input()
        self.assertEqual(sentence, "this _ works!")
        self.assertEqual(words, [])  # No words added

    @patch('builtins.input', side_effect=[
        "fill _ this?", "123", "$$%", "validword", "q"])
    def test_invalid_word_inputs(self, mock_input):
        sentence, words = get_user_input()
        self.assertEqual(sentence, "fill _ this?")
        self.assertEqual(words, ["validword"])
