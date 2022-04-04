# Shift Cipher for Small Characters
print("\n*** Shift Cipher ***\n")

def shiftencrypt(msg, key):
	cipher = []
	for m in msg:
		cipher.append(chr((ord(m)-97 + key) % 26 + 97))
	
	return ''.join(cipher)


def shiftdecrypt(cip, key):
	msg = []
	for c in cip:
		msg.append(chr((ord(c)-97 - key) % 26 + 97))
	
	return ''.join(msg)


org1 = input("Enter your text: ")
key = int(input("Enter the key: "))

cip1 = shiftencrypt(org1, key)
msg1 = shiftdecrypt(cip1, key)

print("Original Message: ", org1)
print("Shift Encrypted: ", cip1)
print("Shift Decrypted: ", msg1)

