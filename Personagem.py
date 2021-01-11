class Personagem:
    def __init__(self, vida = 100):
        self.vida = vida

    def receberAtaque(self, dano):
        self.vida -= dano
        if self.vida>0:
            print("Desgracado, ainda estou vivo", "Vida: ", self.vida)

        else:
            print("No ceu tem pao?", "Vida: ", self.vida)

    def enfrentarInimogo(self,lista):
        while len(inimigos)>0:
            ("Numero de inimigos: ", len(lista))
            self.receberAtaque(lista[0].ataque)
            del(lista[0])



class Inimigo:
    def __init__(self,PDAtaque = 50):
        self.ataque = PDAtaque

Personagem1 = Personagem(500)
Inimigo1 = Inimigo(200)
Inimigo2 = Inimigo()
Inimigo3 = Inimigo(100)
inimigos = [Inimigo1, Inimigo2, Inimigo3]

while len(inimigos)>0:
    Personagem1.enfrentarInimogo(inimigos)