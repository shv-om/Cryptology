# Vernam / One time pad Cipher

print("\n*** One time pad/Vernam Cipher ***")

def vernamencrypt(org, key):
	cipstream = []

	for i in range(len(key)):
		new = int(ord(org[i])) ^ int(ord(key[i]))
		# print(int(ord(org[i])), int(ord(key[i])), '-->', new)
		cipstream.append(chr(new + 97))

	return ''.join(cipstream)


def vernamdecrypt(cip, key):
	msgstream = []

	for i in range(len(key)):
		new = int(ord(cip[i]) - 97) ^ int(ord(key[i]))
		# print(int(ord(cip[i])), int(ord(key[i])), '-->', new)
		msgstream.append(chr(new))

	return ''.join(msgstream)



print("* Message and Keys should be of equal length")
org1 = input("Enter a text: ")
key = input("Enter a key (random): ")

cip1 = vernamencrypt(org1, key)
msg1 = vernamdecrypt(cip1, key)

print("Original Message:", org1)
print("Vernam Encrypted:", cip1)
print("Vernam Decrypted:", msg1)