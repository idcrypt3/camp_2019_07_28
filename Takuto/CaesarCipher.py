def encode(message):
    result = ""
    for i in range(len(message)):
        char = message[i]
        result +=chr(ord(char)+3)
    return result

message=input("please enter a secret message:")
print(encode(message))

