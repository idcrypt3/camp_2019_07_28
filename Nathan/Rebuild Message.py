def rebuild_message(message_list, block_size=4):
    message = ""
    for i in range(len(message_list)):
        chunk = message_list[i]
        for c in range(block_size):
            number = (chunk >> (8 * (block_size - 1 - c))) % 2 ** 8
            message += chr(number)
    return message


def apply_rotate(message_list, key, block_size=4):
    cipher_list = []
    bit_max = block_size * 8
    for i in range(len(message_list)):
        chunk = message_list[i]
        carry = chunk % (2**key)
        carry = carry << (bit_max - key)
        cipher = (chunk >> key) + carry
        cipher_list.append(cipher)
    return cipher_list


plaintext = "iD Tech Camps"
key = 10
text_list = pad_message(plaintext)
cipher_list = apply_rotate(text_list, key)
cipher = rebuild_message(cipher_list)
print(cipher)

message_list = undo_rotation(cipher_list, key)
message = rebuild_message(message_list)

