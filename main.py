from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from typing import Tuple


def select_cypher_decypher() -> str:
    while True:
        chosen_type = input("Choose Cypher/Decypher: ")
        if chosen_type.lower() in ["cypher", "decypher"]:
            return chosen_type
        else:
            print(f"Error: Your entered type must be Cypher or Decypher")

def select_text() -> bytes:
    return input("Type in your text: ").encode('utf-8')

def select_key() -> bytes:
    while True:
        key = input("Enter a 128-bit (16-byte) key: ").encode('utf-8')
        if len(key) == 16:
            return key
        else:
            print(f"Error: Your entered key length {len(key)}. Key must be exactly 16 bytes long.")

def user_input() -> Tuple[str, str, bytes]:
    return select_cypher_decypher(), select_text(), select_key()

def main():
    chosen_type, text_to_process, secret_key = user_input()

    cipher = AES.new(secret_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(pad(text_to_process, AES.block_size))

    if chosen_type.lower() == "cypher":
        print(f"Encypted text: {ciphertext}")
    elif chosen_type.lower() == "decypher":
        print()

if __name__ == "__main__":
    main()
