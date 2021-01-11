class Quadrado():

    def __init__(self,pLado):
        self.lado = pLado

    def calcularArea(self):
        return self.lado*self.lado

    def retornarLado(self):
        return self.lado

LadoQuad = int(input("Digite o lado do quadrado"))

quad = Quadrado(LadoQuad)

print(quad.calcularArea())
print(quad.retornarLado())
novoLado = int(input("Digite o novo valor do lado"))
quad.lado = novoLado
print(quad.calcularArea())
print(quad.retornarLado())