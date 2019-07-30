import alphabet as alphabet

Message=input("Please enter a message to encrypt:")
Message=input("...").lower()
key=input("Enter Key to Shift")
key=int(input("..."))
if key==0:
    newAlphabet = alphabet
elif key>0:
    partialOne = alphabet[:key]
    partialTwo = alphabet[key:]
    newAlphabet = partialOne+partialTwo
    partialOne.append(partialTwo)
else:
      alphabet[:(26+key)]
      partialTwo = alphabet[(26 + key):]
      newAlphabet=partialTwo+partialOne