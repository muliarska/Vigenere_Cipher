"""Represents a VigenereCipher class"""
from re import sub
import string


class VigenereCipher:
    """Represents The Vigenere cipher,
    a way of encrypting alphabetic text"""
    def __init__(self, keyword):
        """
        (str) ->
        Initialize a keyword
        """
        self.keyword = keyword

    @staticmethod
    def _check_text(text):
        """
        (str) -> str/None
        Returns uppercase text without space characters
        """
        text = sub("[\\d,\\W]", "", text).upper()
        for letter in text:
            if letter not in string.ascii_uppercase:
                return None
        return text

    def _extend_keyword(self, size):
        """
        (int) -> str
        Returns a word that consist of many words keyword,
        the length of the result word >= size
        """
        keyword = self._check_text(self.keyword)
        if keyword is None:
            return None
        extended = ""
        while len(extended) < size:
            extended += keyword
        return extended

    def _code_process(self, text, code_operation):
        """
        (str, str) -> str/None
        Represents a process of encoding and decoding using
        the Vigenere cipher and returns a result text
        """
        text = self._check_text(text)
        if text is None or text == '':
            return None

        keyword = self._extend_keyword(len(text))
        if keyword is None:
            return None

        result_text = ""

        for i in enumerate(text):
            letter_ord = ord(i[1]) - ord("A")
            keyword_ord = ord(keyword[i[0]]) - ord("A")
            if code_operation == "+":
                result_text += chr(ord("A") + (letter_ord + keyword_ord) % 26)
            else:
                result_text += chr(ord("A") + (letter_ord - keyword_ord) % 26)

        return result_text

    def encode(self, plaintext):
        """
        (str) -> str
        Encodes a plaintext and returns a result text
        """
        return self._code_process(plaintext, "+")

    def decode(self, ciphertext):
        """
        (str) -> str
        Decodes a ciphertext and returns a result text
        """
        return self._code_process(ciphertext, "-")
