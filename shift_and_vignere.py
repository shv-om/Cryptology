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
cip1 = shiftencrypt(org1, 4)
msg1 = shiftdecrypt(cip1, 4)

print("Original Message: ", org1)
print("Shift Encrypted: ", cip1)
print("Shift Decrypted: ", msg1)


# Vignere Cipher
print("\n*** Vignere Cipher ***\n")

def vigencrypt(msg, key):
	cip = []
	for i in range(len(msg)):
		n = ord(msg[i]) - 97
		k = ord(key[i % len(key)]) - 97
		cip.append(chr((n + k) % 26 + 97))
	
	return ''.join(cip)

def vigdecrypt(cip, key):
	msg = []
	for i in range(len(cip)):
		n = ord(cip[i]) - 97
		k = ord(key[i % len(key)]) - 97
		msg.append(chr((n - k) % 26 + 97))
	
	return ''.join(msg)


org2 = input("Enter the text: ")
key = input("Enter the key: ")
cip2 = vigencrypt(org2, key)
msg2 = vigdecrypt(cip2, key)

print("Original Message: ", org2)
print("Vignere Encrypted: ", cip2)
print("Vignere Decrypted: ", msg2)







