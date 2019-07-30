alphabet = "abcdefghijklmnopqrstuvwxyz"
partialOne = ""
partialTwo = ""
newAlphabet = ""
Message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"
Message = input("Please enter a message to encrypt:").lower()
key = int(input("Enter Key to Shift"))
if key == 0:
    newAlphabet = alphabet
elif key > 0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialOne+partialTwo
else:
    partialOne = alphabet[:(26 + key)]
    partialTwo = alphabet[(26 + key):]
    newAlphabet=partialTwo+partialOne
newMessage = ""
for i in range(0,len(Message)):
    index = alphabet.find(Message[i])
if index <0:
    newMessage += Message[i]
else:
    newMessage += newAlphabet[index]
