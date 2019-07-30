alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
message = input("Please enter a secret message: ")
message = input(" ... ").lower()
key = input("Please enter a number to shift by: ")
key = int(input(" ... "))
if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialTwo + partialOne
else:
    partialOne = alphabet[:26 + key]
    partialTwo = alphabet[(26 + key):]
    newAlphabet = partialTwo + partialOne