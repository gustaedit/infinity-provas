""" Considere o seguinte dicionário em Python:

pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

a) Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.

b) Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.

c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.

sua resposta """
pessoas = {
    "João": 23,
    "Maria": 28,
    "Pedro": 35,
    "Lucas": 19
}

idade_joao = pessoas["João"]
print("Idade de João:", idade_joao)

pessoas["Ana"] = 31
print("Dicionário após adicionar Ana:", pessoas)

def maior_idade(dic):
    maior_nome = ""
    maior_idade = 0

    for nome, idade in dic.items():
        if idade > maior_idade:
            maior_idade = idade
            maior_nome = nome

    return maior_nome

nome_maior_idade = maior_idade(pessoas)
print("Nome da pessoa com maior idade:", nome_maior_idade)
