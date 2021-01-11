import random

erros = 0
continua_jogo = True
lista_palavras = ["diagonal","egito","armadilha","sombra","tempestade","bussola","fisica","republica","escrita","anatomia"]
palavra = random.choice(lista_palavras)
print(palavra)
mostra_palavra = []
for i in palavra:
    mostra_palavra.append("_")

print("Bem vindo ao jogo da forca")
print("A sua palavra tem", len(palavra), "letras")

while (continua_jogo):
    print("Erros:", erros)
    for i in range(len(palavra)):
        print(mostra_palavra[0], end=" ")
    print(" ")
    palpite = input("Digite o seu palpite ou a resposta")
    if len(palpite) > 1:
        if (palpite == palavra):
            print("Voce acertou")
            continua_jogo = False
        else:
            print("Palpite errado")
    elif len(palpite)==1:
        if palpite in palavra:
            print("Você acertou uma letra")
            for i in range(len(palavra)):
                if (palavra[i] == palpite):
                    mostra_palavra[i] = palpite
        else:
            print("Você errou")
            erros+=1
    elif (erros >5):
        print("Você perdeu")
        continua_jogo = False

