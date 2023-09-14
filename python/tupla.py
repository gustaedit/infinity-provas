""" Escreva um programa em Python que receba duas listas como entrada do usuário e
retorne uma tupla contendo os elementos em comum entre as duas listas e a soma desses elementos. 

sua resposta"""
def elementos_em_comum_e_soma(lista1, lista2):
    elementos_comuns = []
    soma_elementos = 0

    for elemento in lista1:
        if elemento in lista2:
            elementos_comuns.append(elemento)
            soma_elementos += elemento

    return elementos_comuns, soma_elementos

lista1 = [int(x) for x in input("Digite os elementos da primeira lista separados por espaço: ").split()]
lista2 = [int(x) for x in input("Digite os elementos da segunda lista separados por espaço: ").split()]

resultados = elementos_em_comum_e_soma(lista1, lista2)
elementos_comuns, soma_elementos = resultados

print("Elementos em comum:", elementos_comuns)
print("Soma dos elementos em comum:", soma_elementos)
