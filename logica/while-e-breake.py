""" Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência até que ele acerte.
 Para ajudar o usuário, o programa deve informar se o número é maior ou menor que o número a ser adivinhado. Ao final,
   imprima o número adivinhado e a quantidade de tentativas.


Faça uma saída personalizada para cada situação utilizando um dos métodos de formatação de string. 

Sua resposta:"""

import random



numero_a_ser_adivinhado = random.randint(1, 100)



tentativas = 0



while True:

    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))

    tentativas += 1



    if tentativa < numero_a_ser_adivinhado:

        print("O número é maior. Tente novamente.")

    elif tentativa > numero_a_ser_adivinhado:

        print("O número é menor. Tente novamente.")

    else:

        print(f"Parabéns! Você acertou o número {numero_a_ser_adivinhado} em {tentativas} tentativas.")

        break