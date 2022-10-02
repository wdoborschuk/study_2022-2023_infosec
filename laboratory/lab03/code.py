# --- Modules ---

import numpy as np

# --- Functions ---

# Cyrillic or Latin alphabet getter
def get_alphabet(option="eng"):
    if option == "eng":
        return list(map(chr, range(ord("a"), ord("z")+1)))
    elif option == "rus":
        return list(map(chr, range(ord("а"), ord("я")+1)))

# Gamma Encryption
def gamma_encryption(message: str, gamma: str):
    alphabet = get_alphabet()
    if message.lower() not in alphabet:
        alphabet = get_alphabet("rus")
    
    print(alphabet)
    m = len(alphabet)

    def encrypt(letters_pair: tuple):
        idx = (letters_pair[0] + 1) + (letters_pair[1] + 1) % m
        if idx > m:
            idx = idx - m

        return idx - 1
        
    message_cleared = list(filter(lambda s: s.lower() in alphabet, message))
    gamma_cleared = list(filter(lambda s: s.lower() in alphabet, gamma))
    
    message_indices = list(map(lambda s: alphabet.index(s.lower()), message_cleared))
    gamma_indices = list(map(lambda s: alphabet.index(s.lower()), gamma_cleared))
    
    for i in range(len(message_indices) - len(gamma_indices)):
        gamma_indices.append(gamma_indices[i])

    print(f'{message.upper()} -> {message_indices}\n{gamma.upper()} -> {gamma_indices}')

    encrypted_indices = list(map(lambda s: encrypt(s), zip(message_indices, gamma_indices)))
    print(f"ENCRYPTED FORM: {encrypted_indices}\n")
    
    return ''.join(list(map(lambda s: alphabet[s], encrypted_indices))).upper()

def test_encryption(message: str, gamma: str):
    print(f'ENCRYPTION RESULT: {gamma_encryption(message, gamma)}')

# --- Main ---

def main():
    message = "приказ"
    gamma = "гамма"

    print("TEST 1\n")
    test_encryption(message, gamma)

    message = "Шла Саша по шоссе и сосала сушку"
    gamma = "Котопес"

    print("TEST 2\n")
    test_encryption(message, gamma)

if __name__ == "__main__":
    main()
