def rr(word, count)
    return ((word >> count) | (word << (32 - count))) % 2**32