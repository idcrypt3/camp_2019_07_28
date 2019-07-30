code_ints = [int(i) for i in str(100110110111001110010101)]
key_ints = [int(i) for i in str(100010010101011011010101)]
cipher_ints = []
for x in range(len(code_ints)):
    cipher_bit = code_ints[x] ^ key_ints[x]
cipher_ints.append(cipher_bit)
cipher = "".join(str(b) for b in cipher_ints)
print(cipher)
