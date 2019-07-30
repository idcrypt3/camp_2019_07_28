def rr(word, count):
    return((word >> count) | (word << (32 - count)))%2**32
def ch(e,f,g):
    return (e&f)^((~e)&g)
def maj(a, b, c):
    return(a&b)^(a&c)^(b&c)
def Sigo(word):
    return rr(word, 2)^rr(word, 13)^rr(word, 22)
def Sig1(word):
    return rr(word, 6)^rr(word, 11)^rr(word, 25)
def sigo(word):
    return rr(word, 7)^rr(word, 18)^(word >>3)
def sig1(word):
    return rr(word, 17)^ rr(word,  19)^(word>> 10)
def pad_message(message):
    message_int = 0
    L = len(message)*8
    for c in range(len(message)):
        message_int = message_int << 8
        message_int += ord(message[c])
    message_int = (message_int << 1) + 1
    filler_zeroes = 512 - ((L + 1 + 64)%512)
    message_int = (message_int << 64) + L
    return message_int
def SHA256(message: int):
    hash_list = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    chunk_count = (message.bit_length() - 1) // 512 + 1
    for i in range(chunk_count):
        chunk = (message >> (512*(chunk_count - 1 - i)))% 2**512
        word_array = []
        for w in range(16):
            word = (chunk >> (32*(15 - w)))%2**32
            word_array.append(word)
        for w i range(16, 64):
