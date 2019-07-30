def rr(word, count):
    return ((word >> count) | (word << (32 - count))) % 2 ** 32


def ch(e, f, g):
    return (e & f) ^ ((~e) & g)


def maj(a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)


def s0(word):
    return rr(word, 2) ^ rr(word, 13) ^ rr(word, 22)


def s1(word):
    return rr(word, 6) ^ rr(word, 11) ^ rr(word, 25)


def a0(word):
    return rr(word, 2) ^ rr(word, 13) ^ rr(word, 22)


def a1(word):
    return rr(word, 6) ^ rr(word, 11) ^ rr(word, 25)


def pad_message(message):
    L = len(message) * 8
    message_int = 0
    for c in range(len(message)):
        message_int = message_int << 8
        message_int += ord(message[c])
    message_int = (message_int << 1) + 1
    filler_zeroes = 512 - ((L + 65) % 512)
    message_int = message_int << filler_zeroes
    message_int = (message_int << 64) + L
    return message_int
def sha256(message):
    hash_list = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    k = [BIG CHUNK OF NUMBERS]
    chunk_count = (message.bit_length() - 1) // 512 + 1
    for i in range(chunk_count):
        chunk = (message >> (512 * (chunk_count - 1 - i))) % 2 ** 512




