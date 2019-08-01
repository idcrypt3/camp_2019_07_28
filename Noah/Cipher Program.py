import time
print("Project Name: Prometheus")
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
elif prometheuscode == "S7yf@11.":
    print("C'est bien")
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
                number = (chunk >> (8 * (block_size - 1 - c))) % 2 ** 8
                message += chr(number)
        return message


    # def apply_rotate(message_list, key, block_size=4):
    # cipher_list = []
    # bit_max = block_size * 8
    # for i in range(len(message_list)):
    # chunk = message_list[i]
    # carry = chunk % 2**key
    # carry = carry <<(bit_max - key)
    # cipher = (chunk >> key) + carry
    # cipher_list.append(cipher)
    # return cipher_list
    plaintext = input("Please enter input for the block cipher:")
    key = 10
    text_list = pad_message(plaintext)
    print("text_list: {}".format(text_list))
    # cipher_list = apply_rotate(text_list, key)
    # print("cipher_list: {}".format(cipher_list))
    cipher = rebuild_message(text_list)
    print("decoded: {}".format(cipher))
elif prometheuscode == "G00d3orn!ng":
    def apply_shift(message, key):
        cipher = ""
        for c in message:
            number = ord(c) + key
            cipher += chr(number)
        return cipher


    def remove_shift(cipher, key):
        message = ""
        for c in cipher:
            number = ord(c) - key
            message += chr(number)
        return message


    def find_shared_key(private_key, public_key):
        shared_key = public_key ** private_key % public_modulus
        return shared_key


    public_base = 8
    public_modulus = 29
    alice_private_key = 5
    bob_private_key = 7
    alice_message = input("Enter DHM message:")
    alice_public_key = public_base ** alice_private_key % public_modulus
    bob_public_key = public_base ** bob_private_key % public_modulus
    alice_shared_key = find_shared_key(alice_private_key, bob_public_key)
    alice_cipher = apply_shift(alice_message, alice_shared_key)
    print(alice_cipher)
    bob_shared_key = find_shared_key(bob_private_key, alice_public_key)
    bob_message = remove_shift(alice_cipher, bob_shared_key)
    print(bob_message)
elif prometheuscode == "S<!enTizt":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = input("What would you like to decrypt:")


    def decode(message):
        for key in range(len(alphabet)):
            newAlphabet = alphabet[key:] + alphabet[:key]
            attempt = ""
            for i in range(len(message)):
                index = alphabet.find(message[i])
                if index < 0:
                    attempt += message[i]
                else:
                    attempt += newAlphabet[index]
            print("Key:" + str(key) + "-" + attempt)
    decode(message)
else:
    malfunction = True
    while malfunction:
        print("MALFUNCTION")
        time.sleep(0.23)