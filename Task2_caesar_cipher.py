# Cyber Security Project 2 By Harini Kasi
# Basic Encryption and Decryption
# Caesar Cipher


def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        if char.isupper():

            encrypted_text += chr(
                (ord(char) - 65 + shift) % 26 + 65
            )

        elif char.islower():

            encrypted_text += chr(
                (ord(char) - 97 + shift) % 26 + 97
            )

        else:
            encrypted_text += char


    return encrypted_text



def decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        if char.isupper():

            decrypted_text += chr(
                (ord(char) - 65 - shift) % 26 + 65
            )


        elif char.islower():

            decrypted_text += chr(
                (ord(char) - 97 - shift) % 26 + 97
            )


        else:
            decrypted_text += char


    return decrypted_text



# User Input

message = input("Enter message: ")

shift = int(input("Enter shift value: "))


# Encryption

encrypted = encrypt(message, shift)


print("\nEncrypted Message:")
print(encrypted)



# Decryption

decrypted = decrypt(encrypted, shift)


print("\nDecrypted Message:")
print(decrypted)