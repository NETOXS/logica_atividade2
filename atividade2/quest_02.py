import math

#função do mdc
def calcular_mdc(a, b):
    return math.gcd(a, b)

#função do mmc
def calcular_mmc(a, b):
    return abs(a * b) // calcular_mdc(a, b)

# Lendo dos valores
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

# Calculando MDC e MMC
mdc = calcular_mdc(a, b)
mmc = calcular_mmc(a, b)

print(f"MDC de {a} e {b} = {mdc}")
print(f"MMC de {a} e {b} = {mmc}")