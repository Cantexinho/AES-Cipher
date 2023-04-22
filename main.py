from ecb_cihper import EcbCipher as Ecb
from cbc_cipher import CbcCipher as Cbc

def select_cipher_decypher() -> str:
    while True:
        chosen_type = input("Choose Cipher/Decipher: ")
        if chosen_type.lower() in ["cipher", "decipher"]:
            return chosen_type
        else:
            print(f"Error: Your entered type must be Cipher or Decipher")

def select_cipher_text() -> bytes:
    return input("Type in your text: ").encode('utf-8')

def select_decipher_text() -> bytes:
    text = input("Type in your text: ")
    return bytes.fromhex(text)


def select_cipher_mode():
    while True:
        chosen_mode = input("Choose one from - ECB, CBC, CFB: ")
        if chosen_mode.lower() not in ["ecb", "cbc", "cfb"]:
            print(f"Error: Your entered type must be ECB, CBC or CFB")
        else:
            if chosen_mode.lower() == "ecb":
                return Ecb()
            if chosen_mode.lower() == "cbc":
                return Cbc()


def main():
    chosen_type = select_cipher_decypher()
    cipher_mode = select_cipher_mode()

    if chosen_type.lower() == "cipher":
        text_to_process = select_cipher_text()
        hex_cipher_text = cipher_mode.cipher_text(text_to_process).hex()
        print(f"Ciphered text: {hex_cipher_text}")
    elif chosen_type.lower() == "decipher":
        text_to_process = select_decipher_text()
        plain_deciphered_text = cipher_mode.decipher_text(text_to_process).decode('utf-8')
        print(f"Deciphered text: {plain_deciphered_text}")



if __name__ == "__main__":
    main()

