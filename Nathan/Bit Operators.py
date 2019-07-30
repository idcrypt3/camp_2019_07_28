"And"
A = 0b1101
B = 0b1010
C = A & B
print(bin(C))
"Or"
D = A | B
print(bin(D))
"Not"
E = ~A
print(bin(E))
"XOR"
F = A ^ B
print(bin(F))
"Shifting"
G = A << 1
H = A >> 2
I = A << 2
print(G)
print(H)
print(I)