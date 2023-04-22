from ecb_cihper import EcbCipher as Ecb
from cbc_cipher import CbcCipher as Cbc
from cfb_cipher import CfbCipher as Cfb
from ofb_cipher import OfbCipher as Ofb

# Using while(true) statements is bad, however bad input can be worse

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
        chosen_mode = input("Choose one from - ECB, CBC, CFB, OFB: ")
        if chosen_mode.lower() not in ["ecb", "cbc", "cfb", "ofb"]:
            print(f"Error: Your entered type must be ECB, CBC, OFB or CFB")
        else:
            if chosen_mode.lower() == "ecb":
                return Ecb()
            if chosen_mode.lower() == "cbc":
                return Cbc()
            if chosen_mode.lower() == "cfb":
                return Cfb()
            if chosen_mode.lower() == "ofb":
                return Ofb()

def should_read_from_file() -> bool:
    while True:
        answer = input("Do you want to read the text from file? (Yes/No) ")
        if answer.lower() not in ["yes", "no"]:
            print(f"Error: Your must say Yes or No!")
        else:
            if answer.lower() == "yes":
                return True
            if answer.lower() == "no":
                return False

def read_from_file(file_name: str) -> str:
    file_name = file_name.strip()
    with open(f"{file_name}.txt", "r") as file:
        content = file.read()
        return bytes.fromhex(content.strip())

def cipher_text(cipher_mode: object) -> str:
    text_to_process = select_cipher_text()
    hex_cipher_text = cipher_mode.cipher_text(text_to_process).hex()
    print(f"Ciphered text: {hex_cipher_text}")
    return hex_cipher_text

def decipher_text(cipher_mode: object) -> str:
    if not should_read_from_file():
        text_to_process = select_decipher_text()
    else:
        file_name = input("Type in the file name: ")
        text_to_process = read_from_file(file_name)
    plain_deciphered_text = cipher_mode.decipher_text(text_to_process).decode('utf-8')
    print(f"Deciphered text: {plain_deciphered_text}")
    return plain_deciphered_text

def write_to_file(text: str) -> None:
    while True:
        answer = input("Do you want to put this text to file? (Yes/No) ")
        if answer.lower() not in ["yes", "no"]:
            print(f"Error: Your must say Yes or No!")
        else:
            if answer.lower() == "yes":
                with open('your_cipher.txt', 'w+') as file:
                    file.write(text)
                    return
            if answer.lower() == "no":
                return         

def main():
    chosen_type = select_cipher_decypher()
    cipher_mode = select_cipher_mode()

    if chosen_type.lower() == "cipher":
        text = cipher_text(cipher_mode)
    elif chosen_type.lower() == "decipher":
        text = decipher_text(cipher_mode)

    write_to_file(text)



if __name__ == "__main__":
    main()

