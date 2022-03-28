# Vernam / One time pad Cipher

# Problem with character mapping and while converting string to int preceeding 0s disappear.


print("\n*** One time pad/Vernam Cipher ***")

import random

def vernamencrypt(org, key):
	cipstream = []
	cip = []

	for i in range(len(key)):

		#cipstream = list(cipstream)

		ostream = bin(ord(org[i])).lstrip('0b')
		kstream = bin(ord(key[i])).lstrip('0b')

		for j in range(len(ostream)):
			# print(int(ostream[j]), int(kstream[j]))
			cipstream.append(str(int(ostream[j]) ^ int(kstream[j])))

		#cipstream = ''.join(map(str, cipstream))

		while cipstream != []:
			ch = ''.join(cipstream[:8])
			cipstream = cipstream[8:]
			cip.append(chr(int(ch, 2) + 97))

	return ''.join(cip)


def vernamdecrypt(cip, key):
	msgstream = []
	msg = []

	for i in range(len(key)):

		ostream = bin(ord(cip[i])).lstrip('0b')
		kstream = bin(ord(key[i])).lstrip('0b')

		for j in range(len(ostream)):
			#print(int(ostream[j]), int(kstream[j]))
			msgstream.append(str(int(ostream[j]) ^ int(kstream[j])))

		while msgstream != []:
			ch = ''.join(msgstream[:8])
			msgstream = msgstream[8:]
			msg.append(chr(int(ch, 2) + 97))

	return ''.join(msg)


print("* Message and Keys should be of equal length")
org1 = input("Enter a text: ")
key = input("Enter a key (random): ")

cip1 = vernamencrypt(org1, key)
msg1 = vernamdecrypt(cip1, key)

print("Original Message:", org1)
print("Vernam Encrypted:", cip1)
print("Vernam Decrypted:", msg1)