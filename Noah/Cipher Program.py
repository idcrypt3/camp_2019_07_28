alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
message = input("Please enter a secret message: ").lower()
key = int(input("Please enter a number to shift your message by:"))
if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne
newMessage = ""
for i in range(0, len(message)):
    index = alphabet.find(message[i])
