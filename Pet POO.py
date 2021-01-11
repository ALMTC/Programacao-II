class Pet():
    def __init__(self,Fome, Tedio):
        self.fome = Fome
        self.tedio = Tedio
        self.jogando = True
        self.humor = self.fome + self.tedio

    def alimentar(self):
        self.fome -= 4
        if(self.fome < 0):
            self.fome = 0

    def brincar(self):
        self.tedio -= 4
        if(self.tedio < 0):
            self.tedio = 0

    def falar(self):
        if (self.humor <= 5):
            print("Estou feliz!")
        elif (self.humor > 5 and self.humor <= 10):
            print("Estou ok")
        elif (self.humor > 10 and self.humor <= 15):
            print("Estou triste")
        else:
            print("Nevermind I'll find someone like you")


    def avancarTempo(self):
        self.fome += 1
        self.tedio += 1
        print("Fome: ", self.fome, "Tedio: ", self.tedio)
        self.humor = self.fome + self.tedio

    def jogar(self, n):
        self.avancarTempo()
        if (n == 1):
            self.brincar()
        elif(n == 2):
            self.alimentar()
        elif(n == 3):
            self.falar()
        elif(n == 0):
            self.jogando = False
        else:
            self.falar()


Gato = Pet(0,0)
while(Gato.jogando == True):
    print("Digite 1 para brincar com o pet")
    print("Digite 2 para alimentar o pet")
    print("Digite 3 para falar o pet")
    print("Digite 0 para encerrar a partida")
    n = int(input())
    Gato.jogar(n)