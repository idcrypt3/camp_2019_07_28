def sign_message(message, key):
    message_int = 0
    for c in message:
        message_int += ord(c)
    a = key[0]
    b = key[1]
    mac_tag = (a*message_int + b)%p
    return mac_tag

p = 491
message = "Hello World"
key = [15, 20]
mac = sign_message(message, key)

def check_mac(old_mac, new_mac):
    if old_mac == new_mac:
        print("Message is valid!")
    else:
        print("Message is compromised!")

    message1 = "Hello World"
    message2 = :"Hello World"
    mac1 = sign_message(message1, key)
    mac2 = sign_message0message2, key)
    chech-mac(mac, mac1)
    check_mac(mac, mac2)
