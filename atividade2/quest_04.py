#4)a)
A = True  
B = False  
C = False  

resultado_a = (A != B) and not C
print(f"a) Sentença verdadeira apenas nas condições dadas: {resultado_a}")

#4)b)
resultado_b = not ((A != B) and not C)
print(f"b) Sentença falsa apenas nas condições dadas: {resultado_b}")