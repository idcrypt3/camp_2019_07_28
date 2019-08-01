def shift_cipher(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo = ""
    newAlphabet = ""
    newMessage = ""
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
    for i in range(len(message)):
        index = alphabet.find(message[i])
        if index < 0:
            newMessage += message[i]
        else:
            newMessage += newAlphabet[index]
    return newMessage

def main():
    message = input("Please enter a secret message: ").lower()
    key = int(input("Please enter a number to shift by: "))
    print(shift_cipher(message, key))

if __name__ == "__main__":
    main()