""" Crie uma classe utilizando os conceitos de POO das aulas passadas.

Para criar sua classe, pense em uma entidade do mundo real que possa ser representada de maneira simples e objetiva. 

Por exemplo, uma classe "Pessoa" poderia ter atributos como nome, idade e endereço, e métodos como cumprimentar e se movimentar.

Já uma classe "Animal" poderia ter atributos como espécie, peso e altura, e métodos como andar e dormir.

sua resposta: """
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0  
        
    def acelerar(self, incremento):
        """Acelera o carro em uma determinada quantidade de km/h."""
        self.velocidade += incremento
        
    def frear(self, decremento):
        """Freia o carro em uma determinada quantidade de km/h."""
        if self.velocidade - decremento >= 0:
            self.velocidade -= decremento
        else:
            self.velocidade = 0
    
    def exibir_informacoes(self):
        """Exibe informações sobre o carro."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade Atual: {self.velocidade} km/h")

meu_carro = Carro("Toyota", "Corolla", 2022, "Prata")
meu_carro.exibir_informacoes()

meu_carro.acelerar(50)
meu_carro.exibir_informacoes()

meu_carro.frear(20)
meu_carro.exibir_informacoes()
