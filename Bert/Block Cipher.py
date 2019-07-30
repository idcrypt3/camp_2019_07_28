def pad_message(message, block_size=4):
message_list = []
    chunk = 0
    block_count = len(message)//block_size + 1
    for c in range(block_count * block_size):
chunk = chunk << 8
    if c < len(message):
    chunk += ord(message[c])
else:
    chunk += 0
if chunk.bit_length()>(block_size - 1)* 8:
    message_list.append(chunk)
    chunk = 0
return message_list
