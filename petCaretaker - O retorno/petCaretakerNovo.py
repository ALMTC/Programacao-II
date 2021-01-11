from random import randint


class Pet():
    countID = 0
    def __init__(self, nome, pFome=0, pTedio=0):
        self.id = Pet.countID
        self.nome = nome
        self.__fome = pFome
        self.__tedio = pTedio
        self.__humor = self.__fome + self.__tedio
        self.__alive = True
        Pet.countID+=1

    def getFome(self):
        return self.__fome

    def getTedio(self):
        return self.__tedio

    def getHumor(self):
        return self.__humor

    def setFome(self, novoValor):
        self.__fome = novoValor
        if (self.__fome < 0):
            self.__fome = 1

    def setTedio(self, novoValor):
        self.__tedio = novoValor
        if (self.__tedio < 0):
            self.__tedio = 0

    def isAlive(self):
        return self.__alive

    def avancarTempo(self):
        self.__fome += 1
        self.__tedio += 1
        self.__humor = self.__fome + self.__tedio
        if (self.__humor > 15):
            print("Adeus mundo cruel")
            self.__alive = False

    def falar(self):
        humorDoPet = self.getHumor()
        if (humorDoPet <= 5):
            print(self.nome, "estah feliz!", humorDoPet)
        elif (humorDoPet > 5 and humorDoPet <= 10):
            print(self.nome, "estah ok", humorDoPet)
        elif (humorDoPet > 10):
            print(self.nome, "estah triste", humorDoPet)

    def alimentar(self, comida):
        self.setFome(self.getFome() - comida)

    def brincar(self, brincadeira):
        self.setTedio(self.getTedio() - brincadeira)

    def salvarPet(self):
        save.write(self.nome)
        save.write("\n")
        save.write(str(self.getFome()))
        save.write("\n")
        save.write(str(self.getTedio()))


    def __str__(self):
        return "O nome do animal é:"+self.nome+"\n"+"Seu id é"+str(self.id)+"\n"+"Seu nivel de fome é:"+str(self.getFome())+"\n"+"Seu nivel de tédio é:"+str(self.getTedio())+"\n"+"Seu humor atual é:"+str(self.getHumor())+"\n"

listaPets = []

print("Digite 1 para iniciar um novo jogo")
print("Digite 2 para carregar o jogo salvo")

entrada = int(input())
nomes = ["auau", "miumiu"]

if (entrada == 1):
    for i in range(randint(1,2)):
        listaPets.append(Pet(nomes[randint(0,1)]))
else:
    save = open("save.txt", "r")
    for i in range(int(save.readline())):
        listaPets.append(Pet(save.readline(), int(save.readline()), int(save.readline())))
    save.close()

print("Total de pets:", len(listaPets))
totalMortes = 0

while (totalMortes < len(listaPets)):
    print("Digite 1 para brincar com o pet")
    print("Digite 2 para alimentar o pet")
    print("Digite 3 para falar o pet")
    print("Digite 0 para encerrar a partida")

    entrada = int(input())

    if (entrada == 1):
        for i in listaPets:
            i.brincar(randint(1, 4))
    elif (entrada == 2):
        for i in listaPets:
            i.alimentar(randint(1, 4))
    elif (entrada == 3):
        print(totalMortes)
        totalMortes = 0
        print("Total de pets:", len(listaPets))
        for i in listaPets:
            if(i.isAlive()):
                print(i)
            else:
                totalMortes+=1
        print(totalMortes)
    elif (entrada == 0):
        save = open("save.txt", "w")
        save.write(str(len(listaPets)))
        save.write("\n")
        for i in listaPets:
            i.salvarPet()
            save.write("\n")
        save.close()
        break
    for i in listaPets:
        i.avancarTempo()
