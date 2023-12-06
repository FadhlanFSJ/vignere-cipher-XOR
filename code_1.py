def encrypt(plaintext, key):
    encrypted_text = ""
    bit_values_plain = []
    bit_values_key = []
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    for i in range(len(plaintext)):
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i]))
        encrypted_text += encrypted_char

        bit_values_plain.append(format(ord(plaintext[i]), '08b'))
        bit_values_key.append(format(ord(key[i]), '08b'))

    return encrypted_text, bit_values_plain, bit_values_key

def decrypt(cipher_text, key):
    plain_text = ""
    bit_values_cipher = []
    bit_values_key = []
    key = key * (len(cipher_text) // len(key)) + key[:len(cipher_text) % len(key)]

    for i in range(len(cipher_text)):
        plain_char = chr(ord(cipher_text[i]) ^ ord(key[i]))
        plain_text += plain_char

        bit_values_cipher.append(format(ord(cipher_text[i]), '08b'))
        bit_values_key.append(format(ord(key[i]), '08b'))

    return plain_text, bit_values_cipher, bit_values_key

plain_text = input("Masukan text : ")
key = "Informatika"

cipher_text, bit_values_plain, bit_values_key = encrypt(plain_text, key)
print("====================================================")
print(f"\nNilai Bit {list(plain_text)} = {bit_values_plain}")
print(f"\nNilai Bit {list(key)} = {bit_values_key}")
print(f"\nHasil dari Enkripsi {plain_text} = {cipher_text}\n")
print("====================================================")

pt, bit_cipher, bit_key = decrypt(cipher_text, key)

print(f"\nNilai Bit {list(cipher_text)} = {bit_cipher}")
print(f"\nNilai Bit {list(key)} = {bit_key}")
print(f"\nHasil dari Dekripsi {cipher_text} = {pt}\n")
print("====================================================")