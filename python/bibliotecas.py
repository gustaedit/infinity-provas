""" Considere o seguinte trecho de código em Python:

import random



lista = [1, 2, 3, 4, 5]

x = random.choice(lista)



a) Explique o que o código faz.

b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive).

c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive). 

sua resposta

Importa o módulo "random" em Python.

Cria uma lista chamada "lista" com os elementos [1, 2, 3, 4, 5].

Usa a função "random.choice(lista)" para selecionar aleatoriamente um elemento da lista "lista" e
 atribuí-lo à variável "x". Portanto, "x" conterá um dos elementos da lista de forma aleatória.

 Aqui está um trecho de código que usa a função "random" para gerar um número inteiro aleatório entre 10 e 20 :
 """
import random

numero_aleatorio = random.randint(10, 20)
print(numero_aleatorio)

""" Aqui está um trecho de código que usa a função "random" para gerar uma lista com 5
 elementos inteiros aleatórios entre 1 e 100 : """
import random

lista_aleatoria = [random.randint(1, 100) for _ in range(5)]
print(lista_aleatoria)



