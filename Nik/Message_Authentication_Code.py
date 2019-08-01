def sign_message(message, key):
    message_int = 0
    for c in message:
        message_int += ord(c)

    a = key[0]
    b = key[1]
    mac_tag = (a * message_int + b) % p
    return mac_tag


def check_mac(old_mac, new_mac):
    if old_mac == new_mac:
        print("Message is valid!")
    else:
        print("Message is compromised!")



p = 491
message = "Hello World"

key = [15, 20]

mac = sign_message(message, key)


message1 = "Hello world"
message2 = "Hello World"

mac1 = sign_message(message1, key)
check_mac(mac, mac1)

mac2 = sign_message(message2, key)
check_mac(mac, mac2)