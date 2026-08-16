import string

text = input("Enter text: ")
shift = int(input("Enter shift value: "))


def encrypt(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        elif char.isdigit():
            result += str((int(char) + shift) % 10)

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:

        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        elif char.isdigit():
            result += str((int(char) - shift) % 10)

        else:
            result += char

    return result


encrypted_text = encrypt(text, shift)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)