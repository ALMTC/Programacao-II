fome = 0
tedio = 0
humor = fome + tedio
onPlaying = True

def alimentar():
    global fome
    fome -= 4
    if(fome < 0):
        fome = 0

def brincar():
    global tedio
    tedio -= 4
    if(tedio < 0):
        tedio = 0

def falar():
    global humor
    if(humor <= 5):
        print("Estou feliz!", humor)
    elif(humor > 5 and humor <= 10):
        print("Estou ok", humor)
    elif(humor > 10 and humor <= 15):
        print("Estou triste", humor)
    elif(humor > 15):
        print("Nevermind I'll find someone like you", humor)

def avancarTempo():
    global humor, fome, tedio
    fome += 1
    tedio += 1
    humor = fome + tedio

while(onPlaying):
    print("Digite 1 para brincar com o pet")
    print("Digite 2 para alimentar o pet")
    print("Digite 3 para falar o pet")
    print("Digite 0 para encerrar a partida")
    entrada = int(input())
    if (entrada == 1):
        brincar()
    elif(entrada == 2):
        alimentar()
    elif(entrada == 3):
        falar()
    elif(entrada == 0):
        onPlaying = False
    avancarTempo()