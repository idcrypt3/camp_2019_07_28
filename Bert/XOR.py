
code = "1001001010100001"
key = "1001110100010101"
code_ints = [int(i) for i in str(code)]
key_ints = [int(i) for i in str(key)]
cipher_ints = []
for x in range(len(code_ints)):
    cipher_bits = code_ints[x]^key_ints[x]
    cipher_ints.append(cipher_bits)
    cipher = "".join(str(b) for b in cipher_ints)
print(cipher)
