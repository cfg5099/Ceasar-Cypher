def main():
	print("Please enter the phrase to be encrypted or decrypted: ")
	phrase = list(input())

	print("Please enter the key:")
	key = validKey(input())

	print("Are we Encrypting (1) or Decrypting (2)?")
	choice = input()

	if(choice == '1'):
		encrypt(phrase, key)
		pass

	if(choice == '2'):
		decrypt(phrase, key)
		pass

def validKey(key):
	key = int(key)
	if(key > 25):
		key = key % 26;
	return key

def encrypt(phrase, key):
	for x in range(0, len(phrase)):
		charNum  = ord(phrase[x])
		#if upper case
		if(charNum >= 65 and charNum <= 90):
			newchar = chr((charNum + key - 65) % 26 + 65)
			phrase[x] = newchar

		#if lower case
		if(charNum >= 97 and charNum <=122):
			# math = (charNum + key) % 122 + 96
			# print(math)
			newchar = chr((charNum + key - 97) % 26 + 97)
			phrase[x] = newchar
		pass
	newPhrase = "".join(phrase)
	print("The new encrypted phrase is: " + newPhrase)

def decrypt(phrase, key):
	for x in range(0, len(phrase)):
		charNum  = ord(phrase[x])

		#if upper case
		if(charNum >= 65 and charNum <= 90):
			num = charNum - key - 122
			
			if(num < 0):
				num = num * -1;

			newchar = chr(num % 26 + 64)
			print(newchar)
			phrase[x] = newchar

		#if lower case
		if(charNum >= 97 and charNum <=122):

			newchar = chr((charNum - key - 122) % 26 + 96)
			print(newchar)
			phrase[x] = newchar
		pass
	newPhrase = "".join(phrase)
	print("\n\nThe new encrypted phrase is: " + newPhrase)

if __name__ == '__main__':
	main()