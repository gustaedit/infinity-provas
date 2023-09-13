""" Desenvolva um programa que leia o nome, idade e sexo de 3 pessoas. No final do programa, exiba:

- A média de idade de todo o grupo.

- Qual o nome da pessoa mais velha.

- Quantas pessoas têm menos de 20 anos.

- Quantas pessoas têm mais de 40 anos.

- Qual o sexo da pessoa mais nova.

Sua resposta """

soma_idades = 0
nome_pessoa_mais_velha = ""
idade_pessoa_mais_velha = 0
pessoas_menos_de_20 = 0
pessoas_mais_de_40 = 0
sexo_pessoa_mais_nova = ""

for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")

    soma_idades += idade

    if idade > idade_pessoa_mais_velha:
        nome_pessoa_mais_velha = nome
        idade_pessoa_mais_velha = idade

    if idade < 20:
        pessoas_menos_de_20 += 1

    if idade > 40:
        pessoas_mais_de_40 += 1

    if i == 0 or (idade < idade_pessoa_mais_nova and sexo == "F"):
        sexo_pessoa_mais_nova = sexo
        idade_pessoa_mais_nova = idade

media_idade = soma_idades / 3

print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Pessoa mais velha: {nome_pessoa_mais_velha} (Idade: {idade_pessoa_mais_velha} anos)")
print(f"Pessoas com menos de 20 anos: {pessoas_menos_de_20}")
print(f"Pessoas com mais de 40 anos: {pessoas_mais_de_40}")
print(f"Sexo da pessoa mais nova: {sexo_pessoa_mais_nova}")
