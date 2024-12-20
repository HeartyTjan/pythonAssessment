import unittest
from Assignment import caesarcipher


class CaesarCipherTest(unittest.TestCase):

    def test_encrypt_function_return_encrypted_text(self):
        text = "Codedamn"
        shift = 3
        encrypted_text = caesarcipher.encrypt_text(text, shift)
        expected = "FRGHGDPQ"
        self.assertEqual(encrypted_text, expected)

    def test_decrypt_function_decrypt_encrypted_text(self):
        text = "FRGHGDPQ"
        shift = 3
        decrypted_text = caesarcipher.decrypt_text(text, shift)
        expected = "CODEDAMN"
        self.assertEqual(decrypted_text, expected)
