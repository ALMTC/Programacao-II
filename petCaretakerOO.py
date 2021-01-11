class Pet():
    def __init__(self, pFome=0, pTedio=0):
        self.fome = pFome
        self.tedio = pTedio
        self.humor = self.fome + self.tedio

    def falar(self):
        if (self.humor <= 5):
            print("Estou feliz!", self.humor)
        elif (self.humor > 5 and self.humor <= 10):
            print("Estou ok", self.humor)
        elif (self.humor > 10 and self.humor <= 15):
            print("Estou triste", self.humor)
        elif (self.humor > 15):
            print("Nevermind I'll find someone like you", self.humor)

    def avancarTempo(self):
        self.fome += 1
        self.tedio += 1
        self.humor = self.fome + self.tedio

class Dog(Pet):
    def __init__(self, pFome=0, pTedio=0, pLeseira=0):
        super(Dog, self).__init__(pFome, pTedio)
        self.leseira = pLeseira

    def alimentar(self):
        self.fome -= 2
        if (self.fome < 0):
            self.fome = 0

    def brincar(self):
        self.tedio -= 4
        if (self.tedio < 0):
            self.tedio = 0

class Cat(Pet):
    def __init__(self, pFome=0, pTedio=0, pZZZ=0):
        super(cat, self).__init__(pFome, pTedio)
        self.zzz = pZZZ

    def alimentar(self):
        self.fome -= 4
        if (self.fome < 0):
            self.fome = 0

    def brincar(self):
        self.tedio -= 2
        if (self.tedio < 0):
            self.tedio = 0

onPlaying = True
dog = Dog(2,4,10)
cat = Cat(4,2,10)
animal = raw_input(("Com qual animal voce quer jogar? cat ou dog"))

while (onPlaying):
    print("Digite 1 para brincar com o pet")
    print("Digite 2 para alimentar o pet")
    print("Digite 3 para falar o pet")
    print("Digite 4 para trocar de pet")
    print("Digite 0 para encerrar a partida")
    entrada = int(input())
    if (animal == "dog"):
        if (entrada == 1):
            dog.brincar()
        elif (entrada == 2):
            dog.alimentar()
        elif (entrada == 3):
            dog.falar()
        elif (entrada == 4):
            animal = raw_input(("Com qual animal voce quer jogar? cat ou dog"))
        elif (entrada == 0):
            onPlaying = False
        dog.avancarTempo()
    elif (animal == "cat"):
        if (entrada == 1):
            cat.brincar()
        elif (entrada == 2):
            cat.alimentar()
        elif (entrada == 3):
            cat.falar()
        elif (entrada == 4):
            animal = raw_input(("Com qual animal voce quer jogar? cat ou dog"))
        elif (entrada == 0):
            onPlaying = False
        cat.avancarTempo()