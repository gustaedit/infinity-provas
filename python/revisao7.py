""" Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a média aritmética das notas. Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos alunos até que ele decida parar. Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.
 

Observações:

a) Escreva o código para a função que calcule a média aritmética das notas.

b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

c) Escreva o código para o loop for que imprime a média de cada aluno.

sua Resposta"""

notas_alunos = []


def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


while True:
    try:
        nota = float(input("Insira a nota do aluno (ou digite -1 para encerrar): "))

        if nota == -1:
            break

        notas_alunos.append(nota)
    except ValueError:
        print("Por favor, insira uma nota válida.")


for i, nota in enumerate(notas_alunos, start=1):
    print(f"Média do Aluno {i}: {nota}")


media_turma = calcular_media(notas_alunos)
print(f"Média da Turma: {media_turma}")
