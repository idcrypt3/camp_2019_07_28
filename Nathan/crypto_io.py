import os
import io

# uncomment the 3 lines below and replace the names of your files (do not include .py) and function defs
# leave "as name" as-is; this renames your functions so they are all compatible with this program,
# regardless of what you named them
from Ceaser_Cipher import ceaser_cipher as shift_cypher
from Block_Cipher import pad_message as block_pad, rebuild_message as block_rebuild
from Block_Cipher import apply_rotate as block_shift, undo_rotation as block_unshift
from Diffie_Hellman import find_shared_key as dh_shared_key, apply_shift as dh_shift, remove_shift as dh_unshift

# here I set the private key used in Diffie-Hellman encryptions. Feel free to change it.
# the public_base is set to 8 and public_modulus 29, as on GamePlan. You can change those too.
dh_base = 8
dh_mod = 29
dh_private_key = 49
dh_public_key = dh_base ** dh_private_key % dh_mod

csi = "\x1b["
colorw = "30m"
colorr = "31m"
colorg = "34m"

text1 = "Hello iD Campers, Parents, and Staff!"
text2 ="Welcome to the iD Cryptography Package, cryptoIO!!"
text3 ="Here you can encrypt messages and save them for others to read."
text4 ="But they will only be able to decrypt them if you (remember and) share the secret keys!"


colored_text1 = csi + colorw + text1
colored_text2 = csi + colorw + text2
colored_text3 = csi + colorw + text3
colored_text4 = csi + colorw + text4
colored_text5 = csi + colorw
colored_text6 = csi + colorr
colored_text7 = csi + colorw
colored_text8 = csi + colorw
colored_text9 = csi + colorr
colored_text10 = csi + colorg
colored_text11 = csi + colorw
colored_text12 = csi + colorr
colored_text13 = csi + colorw
colored_text14 = csi + colorr
colored_text15 = csi + colorg
colored_text16 = csi + colorw
colored_text17 = csi + colorw
colored_text18 = csi + colorw
colored_text19 = csi + colorr
colored_text20 = csi + colorw
colored_text21 = csi + colorw
colored_text22 = csi + colorr
colored_text23 = csi + colorw
colored_text24 = csi + colorr
colored_text25 = csi + colorw
colored_text26 = csi + colorr  


def prgreen(skk): print("\033[1;32;00m{}".format(skk))


def main():
    # Feel free to change this intro msg to whatever you want
    print(text1)
    print(text2)
    print(text3)
    print(text4)

    # infinite loop runs until the user quits
    while True:
        print()  # newline for readability
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
            print("Thank you for using iD Tech cryptoIO!")
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
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease s"
            "elect a cypher (1, 2, or 3): ")

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
            msg_public_key = dh_base ** data[1] % dh_mod
            shared_key = dh_shared_key(dh_private_key, msg_public_key)
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
            "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a"
            " cypher (1, 2, or 3): ")

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
            shared_key = dh_shared_key(data[1], dh_public_key)
            decrypted = dh_unshift(data[0], shared_key)
            break
        elif cypher == 0:
            return

    print("The decrypted message is:\n'{}'".format(decrypted))

    return


def get_decrypt_input():
    localmsgs = os.listdir("msgs")
    for i in range(len(localmsgs)):
        n = i + 1  # '0' is the choice for manual input, so we offset the count by +1
        padding = " "
        if n <= 99:
            padding += " "
        if n <= 9:
            padding += " "
        print("{}{}: {}".format(n, padding, localmsgs[i]))
    print()

    while True:
        choice = input("Please choose a message from above to decrypt (or, type 0 for manual entry): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localmsgs)))
            continue

        if choice == 0:
            msg = input("Manually enter the encrypted message: ").strip()
            break
        elif choice <= len(localmsgs):
            with io.open("msgs/{}".format(localmsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print("Sorry, {} is not a valid choice. Pick between 0 and {}.".format(choice, len(localmsgs)))

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


# This line automatically runs the main def when you start the program.
if __name__ == "__main__":
    main()


# Ideas for new features:
# - Include your name or contact info in the comments and/or opening scroll.
# - Write some messages or stories and encrypt and save them to disk for your family and friends to discover.
# - Include color codes - red for failed encryption, green for passed (see the lesson Hexadecimal\Character Codes).
# - This program includes functionality you haven't seen in the form of file I/O, string formatting, and imported
# modules. See if you understand what's going on and reference the online documentation if you don't.
# - Errors are handled, but the user navigation could be more friendly (e.g. allowing users to return to a previous menu
# rather than forcing them to stick with the choice to encrypt or decrypt, even if they change their mind). Try expand-
# ing it!
# Prevent the user from attempting a Ceaser shift greater than +-26, or use mod (%) to correct it

# Advanced features:
# - Create a puzzle for users to solve by slowly ramping up the difficulty (e.g., the key to a block cypher could be
# written in a ceaser cypher (as a word - remember, our ceaser cypher only substitutes letters), and that block cypher
# could have a clue to a Diffie-Hellman cypher, and...)
# - Display the checksum or hash of messages as they are encrypted and decrypted.
# You could even save the checksum/hash alongside the messages, so users know if a file has been modified.
# - Expand your cyphers with more options, or write a new one from internet tutorials.
