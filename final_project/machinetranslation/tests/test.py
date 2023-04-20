import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('wife'), 'épouse')


class TestF2E(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('épouse'), 'wife')


unittest.main()