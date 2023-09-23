""" Desenvolva um exemplo de aplicação de polimorfismo utilizando super classe.

Crie uma classe pai que defina um método genérico, e em seguida crie duas ou mais classes filhas que herdem essa super classe

e sobrescrevam o método de acordo com suas necessidades.

sua resposta """
class Animal:
    def fazer_som(self):
        print("Este animal faz um som genérico")

class Cachorro(Animal):
    def fazer_som(self):
        print("O cachorro late: Woof! Woof!")

class Gato(Animal):
    def fazer_som(self):
        print("O gato mia: Meow! Meow!")


animal_generico = Animal()
marley = Cachorro()
gordinha = Gato()


animal_generico.fazer_som()  
marley.fazer_som()             
gordinha.fazer_som()        