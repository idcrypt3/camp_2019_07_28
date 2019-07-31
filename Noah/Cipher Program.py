"""print("Project Name: Prometheus")
prometheuscode = input("ENTER PASSWORD:")
if prometheuscode == "H@11eluj4h!":
    print("C'est bien.")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    partialOne = ""
    partialTwo = ""
    newAlphabet = ""
    message = input("Please enter a secret message: ").lower()
    key = int(input("Please enter a number to shift your message by:"))
    if key == 0:
        newAlphabet = alphabet
    elif key > 0:
        partialOne = alphabet[:key]
        partialTwo = alphabet[key:]
        newAlphabet = partialTwo + partialOne
    else:
        partialOne = alphabet[:(26 + key)]
        partialTwo = alphabet[(26 + key):]
        newAlphabet = partialTwo + partialOne
    newMessage = ""
    for i in range(0, len(message)):
        index = alphabet.find(message[i])
        if index < 0:
            newMessage += message[i]
        else:
            newMessage += newAlphabet[index]
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print("processing...")
    print(newMessage)
else:
    malfunction = True
    while malfunction:
        print("MALFUNCTION")"""

def pad_message(message, block_size=4):
    message_list = []
    chunk = 0
    block_count = len(message) // block_size + 1
    for c in range(block_count * block_size):
        chunk = chunk << 8
        if c < len(message):
            chunk += ord(message[c])
        else:
            chunk += 0
        if chunk.bit_length() > (block_size - 1) * 8:
            message_list.append(chunk)
            chunk = 0
    return message_list
def rebuild_message(message_list, block_size=4):
    message = ""
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk >> (8 * (block_size - 1 - c))) % 2**8
            message += chr(number)
    return message
"""def apply_rotate(message_list, key, block_size=4):
    cipher_list = []
    bit_max = block_size * 8
    for i in range(len(message_list)):
        chunk = message_list[i]
        carry = chunk % 2**key
        carry = carry <<(bit_max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
        return cipher_list"""
plaintext = input("Please enter input for the block cipher:")
key = 10
text_list = pad_message(plaintext)
print("text_list: {}".format(text_list))
#cipher_list = apply_rotate(text_list, key)
#print("cipher_list: {}".format(cipher_list))
cipher = rebuild_message(text_list)
print("decoded: {}".format(cipher))
