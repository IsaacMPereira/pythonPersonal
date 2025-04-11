import math

class Pessoa:
    class_id = 20 #Class variable
    num_pessoa = 0

    def __init__(self, nome, idade, altura, peso, endereco):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.endereco = endereco
        Pessoa.num_pessoa += 1

    def exibirDados(self):
        print(f"Dados: \nNome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}, Endereco: {self.endereco}")
        print()

    def calcIMC(self):
        imc = self.peso / math.pow(self.altura, 2)

        return imc

class Fazendo:
    class_id = 30

    def __init__(self, ferramenta, objetivo):
        self.ferramenta = ferramenta
        self.objetivo = objetivo

    def fazendo(self):
        print(f"Com {self.ferramenta} fazendo {self.objetivo}")