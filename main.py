print("Please enter the phrase to be encrypted: ")
phrase = list(input())

print("Please enter the key:")
key = input()
key = int(key)

if(key > 25):
	key = key % 26;

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

	# phrase[x] = newchar
	pass

newPhrase = "".join(phrase)
print("The new encrypted phrase is: " + newPhrase)