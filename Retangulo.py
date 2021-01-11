class Ponto():
    def __init__(self,coordx = 0, coordy = 0): # caso não seja especificado, a variável vai ser essa
        self.x = coordx
        self.y = coordy

class Retangulo():

    def __init__(self,Largura = 0, Altura = 0, x = 0, y = 0):
        #atrubutos de classe
        self.largura = Largura
        self.altura = Altura
        self.pontoInicial = Ponto(x, y)

    def calcularArea(self):
        return self.largura * self.altura

    def calcularPerimetro(self):
        return self.largura*2 + self.altura*2

    def clacularCentro(self):
        centroX = self.pontoInicial.x + self.largura/2
        centroY = self.pontoInicial.y - self.altura/2
        return (centroX, centroY)


Base = float(input("Digite a base do retangulo: "))
Altura = float(input("Digite a altura do retangulo: "))

rect = Retangulo(Base, Altura, 20, 20)

Centro = rect.clacularCentro()
print("Ponto central: ", Centro)
print(rect.calcularArea())
print(rect.calcularPerimetro())
Base2 = float(input("Digite a nova base do retangulo: "))
Altura2 = float(input("Digite a nova altura do retangulo: "))
rect.base = Base2
rect.altura = Altura2
print(rect.calcularArea())
print(rect.calcularPerimetro())