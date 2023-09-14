""" Escreva uma função em Python que recebe dois números como argumentos e retorna o maior entre eles.

a) Implemente a função com o nome "maior_numero" e utilizando condicionais.

b) Implemente a mesma função, porém utilizando a função "max".

Sua resposta """
def maior_numero(a, b):

    if a > b:

        return a

    else:

        return b



num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

resultado = maior_numero(num1, num2)

print("O maior número é:", resultado)

def maior_numero(a, b):
    return max(a, b)



