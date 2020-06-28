"""
Unit tests for flask-ops application
"""
import unittest

from app import encrypt_string


class TestApp(unittest.TestCase):
    """
    Test app.py
    """
    def test_encrypt_string_empty(self):
        self.assertEqual(encrypt_string(''),
                         'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855')

    def test_encrypt_string_lower_block_size(self):
        self.assertEqual(encrypt_string('qwerty'),
                         '65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5')

    def test_encrypt_string_equal_block_size(self):
        self.assertEqual(encrypt_string('a' * 64),
                         'ffe054fe7ae0cb6dc65c3af9b61d5209f439851db43d0ba5997337df154668eb')


if __name__ == '__main__':
    unittest.main()
