alphabet="abcdefghijklmnopqrstuvwxyz"
partialOne=""
partialTwo=""
newAlphabet=""
message = input("Please enter a secret message:").lower()
key = int(input("Please enter a number to shift by:"))
if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne
