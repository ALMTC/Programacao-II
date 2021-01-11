class Forma():
    def __init__(self,forma):
        self.forma = forma

    def calculaArea(self):
        if self.forma == "c":
            return self.raio * 3.14
        elif self.forma == "t":
            return (self.base*self.altura)/2
        if self.forma == "q" or "r":
            return self.base*self.altura

    def exibeForma(self):
        if self.forma == "r":
            print("Retangulo")
        elif self.forma == "q":
            print("Quadrado")
        elif self.forma == "t":
            print("Triangulo")
        elif self.forma == "c":
            print("Circulo")

class Quadrado(Forma):
    def __init__(self,forma,base):
        super().__init__(forma)
        self.base = int(base)
        self.altura = int(base)

    def calculaPerimetro(self):
        return 4*self.base

class Rectangulo(Forma):
    def __init__(self,forma,base,altura):
        super().__init__(forma)
        self.base = int(base)
        self.altura = int(base)

    def calculaPerimetro(self):
        return 2*self.base + 2*self.altura

class Triangulo(Forma):
    def __init__(self,forma,base,altura):
        super().__init__(forma)
        self.base = int(base)
        self.altura = int(base)

    def calculaPerimetro(self):
        return self.base + 2*((self.base**2 + self.altura**2)** (1/2))

class Circulo(Forma):
    def __init__(self,forma,raio):
        super().__init__(forma)
        self.raio = int(raio)

testo = open("teste.txt","r")

lista = []
formas = []
for i in testo:
    lista.append(i)

for i in lista:
    if i[0] == "c":
        count = 2
        x = ""
        while i[count]!= " ":
            x += i[count]
            count+=1
        formas.append(Circulo(i[0], x))

print(lista)
for i in formas:
    print(i.raio)
    print(i.calculaArea())
