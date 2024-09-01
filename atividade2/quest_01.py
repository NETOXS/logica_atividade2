# Definindo dos valores das proposições
A = True
B = False
C = True

# a) A ^ (B v C)
resultado_a = A and (B or C)
print(f"a) A ^ (B v C) = {resultado_a}")

# b) (A ^ B) v C
resultado_b = (A and B) or C
print(f"b) (A ^ B) v C = {resultado_b}")

# c) (A ^ B)’ v C
resultado_c = not (A and B) or C
print(f"c) (A ^ B)’ v C = {resultado_c}")

# d) A’ V (B’ ^ C)
resultado_d = not A or (not B and C)
print(f"d) A’ V (B’ ^ C) = {resultado_d}")