from itertools import product

def tabela_verdade(conectivo):
    print("A B | Resultado")
    print("------------")
    for A, B in product([True, False], repeat=2):
        if conectivo == "conjuncao":
            resultado = A and B
        elif conectivo == "disjuncao":
            resultado = A or B
        elif conectivo == "condicional":
            resultado = not A or B
        elif conectivo == "bicondicional":
            resultado = A == B
        elif conectivo == "ou_exclusivo":
            resultado = A != B
        print(f"{A} {B} | {resultado}")

conectivo = input("Digite o conectivo (conjuncao, disjuncao, condicional, bicondicional, ou_exclusivo): ")
tabela_verdade(conectivo)