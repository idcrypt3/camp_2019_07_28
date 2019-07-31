def byte_checksum(message):
    parity_byte = 0
    for c in message:
        parity_byte += ord(c)
        parity_byte = parity_byte % 256
    # Use a not gate so that adding it in during verification produces 0.
    parity_byte = (~parity_byte + 1) % 256
    print(parity_byte)
    return message + chr(parity_byte)


def verify_byte(message):
    parity_check = 0
    for c in message:
        parity_check += ord(c)
        parity_check = parity_check % 256
    if parity_check == 0:
        print("Valid checksum")
    else:
        print("Invalid checksum")


message1 = "Hello"
message2 = byte_checksum(message1)
verify_byte(message2)
verify_byte("HelloT")