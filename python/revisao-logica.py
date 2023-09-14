""" Faça um programa em Python que, utilizando estruturas de repetição, calcule a média de idade dos alunos de uma turma.
 O programa deve pedir ao usuário a quantidade de alunos na turma e, em seguida, solicitar a idade de cada um.
   O programa deve utilizar um laço FOR para receber as idades dos alunos e
 um laço WHILE para realizar a soma das idades. Ao final, o programa deve exibir a média de idade da turma. 

sua resposta"""
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

if quantidade_alunos <= 0:
    print("A quantidade de alunos deve ser maior que zero.")
else:
    soma_idades = 0

    for i in range(1, quantidade_alunos + 1):
        idade = int(input(f"Digite a idade do aluno {i}: "))
        soma_idades += idade

    media_idade = soma_idades / quantidade_alunos
    print(f"A média de idade da turma é: {media_idade:.2f}")
