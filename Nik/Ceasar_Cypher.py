
def Ceasar_Shift(Message,key):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo = ""
    newAlphabet = ""

    if key == 0:
        newAlphabet = alphabet
    elif key > 0:
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
        newAlphabet = partialTwo+partialOne
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
    return newMessage
def main():
    Message = input("Please enter a message to encrypt:").lower()
    key = int(input("Enter Key to Shift"))

    encrypt_message = Ceasar_Shift(Message,key)
    print (encrypt_message)

if __name__ == ("__main__"):
    main()

