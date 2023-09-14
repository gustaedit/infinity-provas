""" Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.


Sua resposta """
def calcular_media(lista):

    if len(lista) == 0:

        return 0

    

    total = sum(lista)

    media = total / len(lista)

    return media



def main():

    numeros = []

    n = int(input("Digite a quantidade de números: "))

    

    for _ in range(n):

        numero = int(input("Digite um número inteiro: "))

        numeros.append(numero)

    

    resultado = calcular_media(numeros)

    print("A média dos números é:", resultado)



if __name__ == "__main__":

    main()