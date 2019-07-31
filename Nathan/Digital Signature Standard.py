def new_hash(message):
    digest = 0
    for c in message:
        digest += ord(c)
        digest = digest % 256
    return digest


def mod_inv(n, modulus):
    q = [0, 0]
    r = [modulus, n]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2] // r[index - 1]
        q.append(quotient)
        remainder = r[index - 2] - q[index] * r[index - 1]
        r.append(remainder)
        aux = a[index - 2] - q[index] * a[index - 1]
        a.append(aux)
        index += 1
    inverse = a[len(a) - 2]
    if inverse < 0:
        inverse += modulus
    return inverse


def sign_message(message):
    k = 48
    r = 0
    s = 0
    while r == 0 or s == 0:
        r = ((g ** k) % p) % q
        if r == 0:
            k += 1
            continue
        s = ((new_hash(message) + x * r) * mod_inv(k, q)) % q
        if s == 0:
            k += 1
            continue
    return [r, s]


q = 191
p = 383
h = 2
g = int(h ** ((p - 1) / q)) % p
x = 29
y = (g ** x) % p
