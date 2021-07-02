# Modified Vigenere Cipher
# - by Shivam

def encrypt(message, key):
    ciphertext = ''
    for i in range(len(message)):
        j = i%4
        if (i+1)%2 == 0:
            message[i] = str(int(message[i]) + int(key[j]))
        ciphertext += str((int(message[i]) + int(key[j])) % 10)

    return ciphertext

def decrypt(cipher, key):
    original = ''
    for i in range(len(cipher)):
        j = i%4
        if (i+1)%2 == 0:
            cipher[i] = str(int(cipher[i]) - int(key[j]))
        original += str((int(cipher[i]) - int(key[j])) % 10)

    return original

#message = input("Enter the Message: ")
#key = input("Enter the key: ")

message = str((10**16)-1)
key = '1636'

cipher = encrypt(list(message), list(key))
original = decrypt(list(cipher), list(key))

print("\n\t" + " * "*5 + " After Encryption " + " * "*5)
print("\n\tCalculated Cipher Message:",cipher)
print("\n\t" + " * "*5 + " After Decryption " + " * "*5)
print("\n\tCalculated Original Message: ", original)
