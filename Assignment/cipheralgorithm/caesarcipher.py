def encrypt_text(text, shift):
    encrypted_text = ""
    for character in text:
        numeric_value = ord(character) - 64 + shift
        encrypted_text += chr(numeric_value + 64)

    return encrypted_text.upper()

def decrypt_text(encrypted_text, shift):
    decrypted_text = ""
    for character in encrypted_text:
        numeric_value = ord(character) - 64 - shift
        decrypted_text += chr(numeric_value + 64)

    return decrypted_text.upper()

