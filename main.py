print("Please enter the phrase to be encrypted: ")
phrase = list(input())

print("Please enter the key:")
key = input()
key = int(key)

if(key > 25):
	key = key % 26;

for x in range(0, len(phrase)):
	charNum  = ord(phrase[x])
	newchar = chr(charNum + key)
	phrase[x] = newchar
	pass

newPhrase = "".join(phrase)
print("The new encrypted phrase is: " + newPhrase)