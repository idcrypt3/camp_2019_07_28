def encrypt(fortnite):
    result = ""
    for i in range(len(fortnite)):
        char = fortnite[i]
        result +=chr(ord(char)+3)
    return result

message=input("please enter a secret message:")
print(encrypt(message))

