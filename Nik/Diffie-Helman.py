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