class CaesarCipher:
    _ALPHABET = [
        ["A", "a"],
        ["B", "b"],
        ["C", "c"],
        ["D", "d"],
        ["E", "e"],
        ["F", "f"],
        ["G", "g"],
        ["H", "h"],
        ["I", "i"],
        ["J", "j"],
        ["K", "k"],
        ["L", "l"],
        ["M", "m"],
        ["N", "n"],
        ["O", "o"],
        ["P", "p"],
        ["Q", "q"],
        ["R", "r"],
        ["S", "s"],
        ["T", "t"],
        ["U", "u"],
        ["V", "v"],
        ["W", "w"],
        ["X", "x"],
        ["Y", "y"],
        ["Z", "z"]
    ]

    def __init__(self, key: int):
        self.alphabet_length = len(self._ALPHABET)
        if key > self.alphabet_length:
            key -= self.alphabet_length
        self.key = key

    def _find_in_alphabet(self, char: str) -> tuple:
        pair_index = -1
        matched_index = -1
        for i in range(self.alphabet_length):
            current_pair = self._ALPHABET[i]
            uppercase_char = current_pair[0]
            lowercase_char = current_pair[1]
            if (char == uppercase_char) or (char == lowercase_char):
                matched_index = self._ALPHABET[i].index(char)
                pair_index = i
        # Return a tuple
        return pair_index, matched_index

    def encrypt(self, plain_text: str) -> str:
        result = ""
        for i in range(len(plain_text)):
            char = plain_text[i]
            if char == " ":
                result += char
                continue
            pair_index, matched_index = self._find_in_alphabet(char)
            new_index = pair_index + self.key
            if new_index > self.alphabet_length:
                new_index -= self.alphabet_length
            # Locate the correct character
            result += self._ALPHABET[new_index][matched_index]
        return result

    def decrypt(self, encrypted_text: str) -> str:
        result = ""
        for i in range(len(encrypted_text)):
            char = encrypted_text[i]
            if char == " ":
                result += char
                continue
            pair_index, matched_index = self._find_in_alphabet(char)
            new_index = pair_index - self.key
            # Locate the correct character
            result += self._ALPHABET[new_index][matched_index]
        return result


if __name__ == "__main__":
    input_msg = input("Enter text: ")
    input_key = int(input("Enter text: "))
    caesar = CaesarCipher(input_key)
    encrypted = caesar.encrypt(input_msg)
    decrypted = caesar.decrypt(encrypted)
    print("Encrypted text: " + encrypted)
    print("Decrypted text: " + decrypted)
