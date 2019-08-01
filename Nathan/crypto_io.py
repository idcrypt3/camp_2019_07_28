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
dh_private_key = 458
dh_public_key = dh_base ** dh_private_key % dh_mod
print(dh_public_key)

csi = "\x1b["
colorw = "30m"
colorr = "31m"
colorg = "36m"
colorc = "37m"
text1 = "Hello iD Campers, Parents, and Staff!"
text2 = "Welcome to the iD Cryptography Package, cryptoIO!!"
text3 = "Here you can encrypt messages and save them for others to read."
text4 = "But they will only be able to decrypt them if you (remember and) share the secret keys!"
text5 = "Type 1 to encrypt, 2 to decrypt, or 0 to quit: "
text6 = "Sorry, that is not a valid choice."
text7 = "Thank you for using iD Tech cryptoIO!"
text8 = "Have a good summer!"
text9 = "Sorry, '{}' is not a valid choice. Pick 1, 2, or 0."
text10 = "Preparing to encrypt..."
text11 = "Please enter your message's name: "
text12 = "Sorry, there is already a secret message with that name. Choose another."
text13 = "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher" \
         " (1, 2, or 3): "
text14 = "Sorry, {} is not a valid choice. Pick 1, 2, or 3."
text15 = "Your message was successfully encrypted!\n"
text16 = "Please enter your secret message: "
text17 = "Preparing to decrypt..."
text18 = "1   : Ceaser (shift) Cypher\n2   : Block Cypher\n3   : Diffie-Hellman Cypher\nPlease select a cypher" \
         " (1, 2, or 3): "
text19 = "Sorry, {} is not a valid choice. Pick 1, 2, or 3."
text20 = "The decrypted message is:\n'{}'"
text21 = "Please choose a message from above to decrypt (or, type 0 for manual entry): "
text22 = "Sorry, {} is not a valid choice. Pick between 0 and {}."
text23 = "Manually enter the encrypted message: "
text24 = "Sorry, {} is not a valid choice. Pick between 0 and {}."
text25 = "Please enter your secret key: "
text26 = "The secret key should be a number. Try again. "
text27 = "Name: Nathan C."
text28 = "Position: Meme master."
text29 = "B, 51 Backwards."

colored_text1 = csi + colorw + text1
colored_text2 = csi + colorw + text2
colored_text3 = csi + colorw + text3
colored_text4 = csi + colorw + text4
colored_text5 = csi + colorw + text5
colored_text6 = csi + colorr + text6
colored_text7 = csi + colorw + text7
colored_text8 = csi + colorw + text8
colored_text9 = csi + colorr + text9
colored_text10 = csi + colorg + text10
colored_text11 = csi + colorw + text11
colored_text12 = csi + colorr + text12
colored_text13 = csi + colorw + text13
colored_text14 = csi + colorr + text14
colored_text15 = csi + colorg + text15
colored_text16 = csi + colorw + text16
colored_text17 = csi + colorw + text17
colored_text18 = csi + colorw + text18
colored_text19 = csi + colorr + text19
colored_text20 = csi + colorg + text20
colored_text21 = csi + colorw + text21
colored_text22 = csi + colorr + text22
colored_text23 = csi + colorw + text23
colored_text24 = csi + colorr + text24
colored_text25 = csi + colorw + text25
colored_text26 = csi + colorr + text26
colored_text27 = csi + colorw + text27
colored_text28 = csi + colorw + text28
colored_text29 = csi + colorc + text29


def prgreen(skk): print("\033[1;32;00m{}".format(skk))


def main():
    # Feel free to change this intro msg to whatever you want
    print(colored_text1)
    print(colored_text2)
    print(colored_text3)
    print(colored_text4)
    print(colored_text29)

    # infinite loop runs until the user quits
    while True:
        print()  # newline for readability
        choice = input(colored_text5)

        try:
            choice = int(choice)
        except:
            print(colored_text6)
            continue

        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            print(colored_text7)
            print(colored_text8)
            print(colored_text27)
            print(colored_text28)
            break
        else:
            print(colored_text9.format(choice))
            continue


def encrypt():
    print(colored_text10)
    data = get_encrypt_input()

    while True:
        file_name = input(colored_text11).strip()
        if "{}.txt".format(file_name) in os.listdir("msgs"):
            print(colored_text12)
            continue

        cypher = input(colored_text13)

        try:
            cypher = int(cypher)
        except ValueError:
            print(colored_text14.format(cypher))
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
    print(colored_text15)


def get_encrypt_input():
    msg = input(colored_text16)
    key = get_key()
    return msg, key


def decrypt():
    print(colored_text17)
    data = get_decrypt_input()

    while True:
        cypher = input(colored_text18)

        try:
            cypher = int(cypher)
        except ValueError:
            print(colored_text19.format(cypher))
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

    print(colored_text20.format(decrypted))

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
        choice = input(colored_text21)

        try:
            choice = int(choice)
        except ValueError:
            print(colored_text22.format(choice, len(localmsgs)))
            continue

        if choice == 0:
            msg = input(colored_text23).strip()
            break
        elif choice <= len(localmsgs):
            with io.open("msgs/{}".format(localmsgs[choice - 1]), 'r', encoding="utf-8") as file:
                msg = file.read()
            break
        else:
            print(colored_text24.format(choice, len(localmsgs)))

    key = get_key()
    return msg, key


def get_key():
    while True:
        try:
            key = int(input(colored_text25))
            break
        except ValueError:
            print(colored_text26)
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
