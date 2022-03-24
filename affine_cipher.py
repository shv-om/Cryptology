# Affine Cipher
print("\n*** Affine Cipher ***")

def inverse(a):
	for i in range(26):
		if i*a % 26 == 1:
			return i


def affine_encrypt(org, a, b):
	cip = []
	for i in org:
		cip.append(chr((((a*(ord(i)-97)) + b) % 26) + 97))

	return ''.join(cip)


def affine_decrypt(cip, a, b):
	msg = []

	for i in cip:
		msg.append(chr(((inverse*((ord(i)-97) - b)) % 26) + 97))

	return ''.join(msg)


org1 = input("Enter a text: ")
a = int(input("Enter a (should be relatively prime to 26): "))
b = int(input("Enter b: "))

inverse = inverse(a)

if not inverse:
	print("'a' is not relatively prime to 26.")
else:
	cip1 = affine_encrypt(org1, a, b)
	msg1 = affine_decrypt(cip1, inverse, b)

	print("Original Message:", org1)
	print("Affine Encrypted:", cip1)
	print("Affine Decrypted:", msg1)