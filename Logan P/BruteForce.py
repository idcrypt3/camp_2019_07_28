message = "wpau iwt ephhldgs udg iwt uxhi rajt xh tctgvxots"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def decode(message):
    for key in range(len(alphabet)):
        newAlphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
        for i in range(len(message)):
            index = alphabet.find(message[i])