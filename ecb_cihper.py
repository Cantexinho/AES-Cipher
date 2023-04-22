from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class EcbCipher:
    def __init__(self) -> None:
        self.key = self.select_key()
    
    def cipher_text(self, text_to_process: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(text_to_process, AES.block_size))
        return ciphertext

    def decipher_text(self, text_to_process: bytes) -> str:
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted_padded_plaintext = cipher.decrypt(text_to_process)
        decrypted_plaintext = unpad(decrypted_padded_plaintext, AES.block_size)
        return decrypted_plaintext
    
    def select_key(self) -> bytes:
        while True:
            key = input("Enter a 128-bit (16-byte) key: ").encode('utf-8')
            if len(key) == 16:
                return key
            else:
                print(f"Error: Your entered key length is {len(key)}. Key must be exactly 16 bytes long.")
