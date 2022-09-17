# --- Ceasar's Cipher ---
def ceasar(letter: chr, key: int, alphabet: list):
    def ceasar(letter: chr, key: int):
        return alphabet.index(letter) + key
    
    if letter.lower() not in alphabet:
        return letter
    
    t_letter = alphabet[ceasar(letter.lower(), key) % len(alphabet)]
    
    if letter.isupper():
        t_letter = t_letter.upper()    
        
    return t_letter

# --- Atbash's Cipher ---
def atbash(letter: chr, alphabet: list):
    if letter.lower() not in alphabet:
        return letter
    
    t_letter = alphabet[len(alphabet) - alphabet.index(letter.lower()) - 1]
    
    if letter.isupper():
        t_letter = t_letter.upper()    
        
    return t_letter

# --- Tests ---
def test_ceasar(message: str, key: int, alphabet: list):
    ciphered_message = list(map(lambda letter: ceasar(letter, key, alphabet), message))
    return "".join(ciphered_message)

def test_atbash(message: str, alphabet: list):
    ciphered_message = list(map(lambda letter: atbash(letter, alphabet), message))
    return "".join(ciphered_message)

# --- Main function ---
def main():
    latin_alphabet = list(map(chr, range(97, 123))) # Latin alphabet list
    cyrillic_alphabet = list(map(chr, range(1072, 1104))) + list(chr(32)) # Cyrillic alphabet list

    latin_message = "Veni, vidi, vici"
    latin_message_new = "Happy New Year, my darling friend!"
    cyrillic_message = "".join(cyrillic_alphabet)
    
    print("\nCEASAR'S CIPHER TEST 1\n-----------")
    print(f"Original: {latin_message}\nCiphered: {test_ceasar(latin_message, 3, latin_alphabet)}\n-----------\n")
    
    print("CEASAR'S CIPHER TEST 2\n-----------")
    print(f"Original: {latin_message_new}\nCiphered: {test_ceasar(latin_message_new, 3, latin_alphabet)}\n-----------\n")
     
    print("ATBASH'S CIPHER TEST STRING OUTPUT\n-----------")
    print(f"Original: {cyrillic_message}\nCiphered: {test_atbash(cyrillic_message, cyrillic_alphabet)}\n-----------\n")
    
    print("ATBASH'S CIPHER TEST LIST OUTPUT\n-----------")
    print(f"Original: {list(cyrillic_message)}\nCiphered: {list(test_atbash(cyrillic_message, cyrillic_alphabet))}\n-----------\n")
    
    
if __name__ == '__main__':
    main()