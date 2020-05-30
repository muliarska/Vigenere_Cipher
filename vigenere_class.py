"""Represents a VigenereCipher class"""
from re import sub


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
        (str) -> str
        Returns uppercase text without space characters
        """
        return sub("\\s", "", text).upper()

    def _extend_keyword(self, size):
        """
        (int) -> str
        Returns a word that consist of many words keyword,
        the length of the result word >= size
        """
        keyword = self._check_text(self.keyword)
        extended = ""
        while len(extended) < size:
            extended += keyword
        return extended

    def _code_process(self, text, code_operation):
        """
        (str, str) -> str
        Represents a process of encoding and decoding using
        the Vigenere cipher and returns a result text
        """
        text = self._check_text(text)
        keyword = self._extend_keyword(len(text))
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
