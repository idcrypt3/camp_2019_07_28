partialOne = ""
partialTwo = ""
newAlphabet = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
def cesar_encrypt(message, key):
    key = key % 26
    message = message.lower()
    if key == 0:
        newAlphabet = alphabet
    elif key > 0:
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
        newAlphabet = partialTwo + partialOne
    else:
        partialOne = alphabet[:(26+key)]
        partialTwo = alphabet[(26+key):]
        newAlphabet = partialTwo + partialOne

    newMessage = ""

    for i in range(0, len(message)):
        index = alphabet.find(message[i])
        if index < 0:
            newMessage += message[i]
        else:
            newMessage += newAlphabet[index]
    return newMessage
def main():
    message = input("Please enter a secret message: ").lower()
    key = int(input("Key: "))
    print(cesar_encrypt(message, key))
if __name__ == "__main__":
    main()
