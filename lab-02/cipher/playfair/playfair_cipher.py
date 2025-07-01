class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_unique = []
        for char in key:
            if char not in key_unique and char.isalpha():
                key_unique.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_unique:
                key_unique.append(letter)

        matrix = [key_unique[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        processed_text = ""
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            if not char1.isalpha():
                i += 1
                continue

            if i + 1 < len(plain_text):
                char2 = plain_text[i + 1]
                if not char2.isalpha():
                    processed_text += char1 + "X"
                    i += 1
                    continue
                if char1 == char2:
                    processed_text += char1 + "X"
                    i += 1
                else:
                    processed_text += char1 + char2
                    i += 2
            else:
                processed_text += char1 + "X"
                i += 1

        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            a, b = processed_text[i], processed_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        # Xử lý loại bỏ 'X' được chèn khi mã hóa
        cleaned = ""
        i = 0
        while i < len(decrypted_text):
            cleaned += decrypted_text[i]
            if i + 2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i + 2] and decrypted_text[i + 1] == 'X':
                i += 2
            else:
                i += 1

        # Bỏ ký tự 'X' cuối nếu không phải là thật
        if len(cleaned) >= 2 and cleaned[-1] == 'X':
            cleaned = cleaned[:-1]

        return cleaned
