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


org = input("Enter the text: ")
key = input("Enter the key: ")
cip = vigencrypt(org, key)
msg = vigdecrypt(cip, key)

print("Original Message: ", org)
print("Vignere Encrypted: ", cip)
print("Vignere Decrypted: ", msg)

