import os, io

from RewritingTheAlphabet import shift_cipher as shift_cypher
from BlockCipher import pad_message as block_pad, rebuild_message as block_rebuild
from BlockCipher import apply_shift as block_shift, undo_shift as block_unshift
from DiffieHellman import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift

dh_base = 8
dh_mod = 29
dh_private_key = 219
dh_public_key = dh_base ** dh_private_key % dh_mod
print(dh_public_key)

def main():
    print("Hello iD Campers, Parents, and Staff!")
    print("Welcome to the iD Cryptography Program, crypto.io!!")
    print("Here you can encrypt messages and save them for others to read.")
    print("But they will only be able to decrypt them if you remember and share the secret keys!")

    while True:
        print()
        choice = input("Type 1 to encrypt, 2 to decrypt, or 0 to quit: ")

        try:
            choice = int(choice)
        except:
            print("Sorry, that is not a valid choice.")
            continue

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            print("Thank you for using crypto.io!")
            print("Have a good summer!")
            break
        else:
            print("Sorry, '{}' is not a valid choice. Pick 1, 2, or 0.".format(choice))
            continue

def encrypt():
    print("Preparing to encrypt...")
    data = get_encrypt_input()

    while True:
        file_name = input("Please enter your message's name: ").strip()
        if "{}.txt".format(file_name) in os.listdir("msgs"):
            print("Sorry, there is already a secret message with that name. Choose another.")
            continue

        cypher = input(
            "1   : Shift Cipher\n2   : Block Cipher\n3   : Diffie-Hellman cipher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, or 3.".format(cypher))
            continue

        if cypher == 1:
            encrypted = shift_cypher(data[0], data[1])
            break
        elif cypher == 2:
            chunk_list = block_pad(data[0])
            encrypted = block_shift(chunk_list, data[1])
            encrypted = "\n".join(str(s) for s in encrypted)
            break
        elif cypher == 3:
            shared_key = dh_shared_key(dh_private_key, data[1])
            encrypted = dh_shift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    with io.open("msgs/{}.txt".format(file_name), 'w+', encoding="utf-8") as file:
        file.write(encrypted)
    print("Your message was successfully encrypted!\n")


def get_encrypt_input():
    msg = input("Please enter your secret message: ")
    key = get_key()
    return msg, key


def decrypt():
    print("Preparing to decrypt...")
    data = get_decrypt_input()

    while True:
        cypher = input(
            "1   : Shift Cipher\n2   : Block Cipher\n3   : Diffie-Hellman Cipher\nPlease select a cypher (1, 2, or 3): ")

        try:
            cypher = int(cypher)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick 1, 2, or 3.".format(cypher))
            continue

        if cypher == 1:
            decrypted = shift_cypher(data[0], -data[1])
            break
        elif cypher == 2:
            chunk_list = list(map(int, data[0].split("\n")))
            chunk_list = block_unshift(chunk_list, data[1])
            decrypted = block_rebuild(chunk_list)
            break
        elif cypher == 3:
            shared_key = dh_shared_key(dh_private_key, data[1])
            decrypted = dh_unshift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    print("The decrypted message is:\n'{}'".format(decrypted))

    return


def get_decrypt_input():
    localMsgs = os.listdir("msgs")
    for i in range(len(localMsgs)):
        n = i + 1
        padding = " "
        if n <= 99:
            padding += " "
        if n <= 9:
            padding += " "
        print("{}{}: {}".format(n, padding, localMsgs[i]))
    print()

    while True:
        choice = input("Please choose a message from above to decrypt (or, type 0 for manual entry): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the encrypted message: ").strip()
            break
        elif choice <= len(localMsgs):
            with io.open("msgs/{}".format(localMsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localMsgs)))

    key = get_key()
    return msg, key


def get_key():
    while True:
        try:
            key = int(input("Please enter your secret key: "))
            break
        except ValueError:
            print("The secret key should be a number. Try again. ")
    return key

if __name__ == "__main__":
    main()