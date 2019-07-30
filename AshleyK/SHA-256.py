def rr(word, count):
    return ((word >> count) | (word << (32 - count))) % 2**32

def ch(e, f, g):
    return (e & f) ^ ((~e) & g)

def maj(a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)

def s0(word):
    return rr(word, 7) ^ rr(word, 18) ^ (word >> 3)

def s1(word):
    return rr(word, 17) ^ rr(word, 19) ^ (word >> 10)

def S0(word):
    return rr(word, 2) ^ rr(word, 13)