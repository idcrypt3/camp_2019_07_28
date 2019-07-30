def rebuild_message(cipher_list, block_size=4):
    message = ""
    for i in range(len(cipher_list)):
        chunk = cipher_list[i]
        for c in range(block_size):
            number = (chunk >> (8 * (block_size - 1 - c))) % 2 ** 8
            message += chr(number)
    return message


def apply_rotate(cipher_list, (bit_max - key), block_size=4):
    message_list = []
    bit_max = block_size * 8
    for i in range(len(cipher_list)):
        chunk = cipher_list[i]
        carry = chunk % (2**(bit_max - key))
        carry = carry << key
        cipher = (chunk >> key) + carry
        message_list.append(cipher)
    return message_list


plaintext = "iD Tech Camps"
key = 10
text_list = pad_message(plaintext)
cipher_list = apply_rotate(text_list, key)
cipher = rebuild_message(cipher_list)
print(cipher)
