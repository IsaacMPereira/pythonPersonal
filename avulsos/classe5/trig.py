class Figura:
    def __init__(self, preenchido):
        self.preenchido = preenchido

class Circulo(Figura):
    def __init__(self, preenchido, raio):
        super().__init__(preenchido)
        self.raio = raio

class Quadrado(Figura):
    def __init__(self, preenchido, largura, altura, diagonal):
        super().__init__(preenchido)
        self.largura = largura
        self.altura = altura

class Triangulo(Figura):
    def __init__(self, preenchido, altura, largura):
        super().__init__(preenchido)
        self.altura = altura
        self.largura = largura

circulo1 = Circulo(preenchido = True, raio = 7)
print(circulo1.preenchido)
print(circulo1.raio)