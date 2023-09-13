""" 
Escreva um código em Python que peça três números e determine:
- O maior número;
- O menor número;
- Se existem números iguais e caso exista, quais são os números.



Sua resposta
 """
def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)

    numeros_iguais = []

    if num1 == num2 or num1 == num3:
        numeros_iguais.append(num1)
    if num2 == num1 or num2 == num3:
        numeros_iguais.append(num2)
    if num3 == num1 or num3 == num2:
        numeros_iguais.append(num3)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")

    if numeros_iguais:
        print("Existem números iguais:")
        for numero in numeros_iguais:
            print(numero)
    else:
        print("Não há números iguais.")

if __name__ == "__main__":
    main()

