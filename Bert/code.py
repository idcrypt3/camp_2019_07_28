def shift_cipher(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo =  ""
    newAlphabet = ""

    if key == 0:
        newAlphabet = alphabet
    elif key > 0:
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
    else:
        partialOne = alphabet[:(26 + key)]
        partialTwo = alphabet[(26 + key)]
        newAlphabet = partialTwo + partialOne
    for i in range(0, len(message)):
        index = alphabet.find(message[i])
    newMessage = ""
    if index < 0:
        newMessage += message[i]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        attempt = ""
        message = "wpau iwt ephhldgs udg iwt uxghi rajt xh tctgvxots"


        def decode(message):
            for key in range(len(alphabet)):
                newAlphabet = alphabet[key:] + alphabet[:key]
                attempt = ""


        for i in range(len(message)):
            index = alphabet.find(message[i])
        else:
            attempt += newAlphabet[index]
    print("Key:" + str(key) + "-" + attempt)
    decode(message)

def main():
    message = input("Please enter a secret message:")
    key = int(input("pass"))
    encrypted = shift_cipher(message, key)
    print(encrypted)
if __name__ == "__main__":
    main()
