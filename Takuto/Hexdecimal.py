def encrypt(fortnite):
    result=""
    for i in range(len(fortnite)):
        char=fortnite[i]
        result+=str(hex(ord(char)))
    return result

message=input("please enter secret message:")
print(encrypt(message))