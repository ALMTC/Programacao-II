import pickle

noMenu = True

class Contato:
    def __init__(self, nome, numero, contatinho):
        self.nome = nome
        self.numero = numero
        self.contatinho = contatinho
        self.mensagem = []

    def receberMensagem(self,msg):
        self.mensagem.append(msg)
        return "Mensagem enviada"


def exibirNomesAlfabetica(list): # Organiza a lista de contatos em ordem alfabédica
    listaN = []
    listaF = []
    for i in list:
        listaN.append(i.nome)
    listaN.sort()
    for i in listaN:
        for j in list:
            if i == j.nome:
                listaF.append(j)
    return listaF

def salva_contatos(): #salva os danos dos contatos completamente
    arquivo = open("contatos.txt", "w+b")
    pickle.dump(lista_de_contatos, arquivo)
    arquivo.close()

def carregar_contatos(): # carrega as informações dos contatos
    global lista_de_contatos
    print("Carregando contatos")
    try:
        arquivo = open("contatos.txt", "rb")
        lista_de_contatos = pickle.load(arquivo)
        arquivo.close()
    except:
        lista_de_contatos = []
        print("Você não possui contatos salvos")

carregar_contatos()

while noMenu:
    print("-" * 5 + "Bem vindo a Agenda" + "-" * 5)
    print("0 - Cadastrar contato")
    print("1 – Deletar contato")
    print("2 – consultar agenda")
    print("3 – Mandar mensagem para o contato")
    print("9 – sair da aplicação")
    opcao = input()

    try:
        opcao = int(opcao)
        if opcao == 0:
            print("Digite o nome do contato:")
            nome = input()
            nome = str(nome)
            nome = nome.strip()
            nome = nome.lower()
            nome1 = nome[0]
            nome1 = nome1.upper()
            nome2 = nome[1:len(nome)]
            nome = nome1+nome2
            count = 1
            nomeF = nome
            for i in lista_de_contatos:
                if nomeF == i.nome:
                    nomeF = nome+str(count)
                    count+=1
            if len(nomeF) == 0:
                nomeF = nome
            print("Digite o número do contato:")
            try:
                numero = int(input())
                print("Esse número é um contatinho?")
                print("1 - sim")
                print("2 = não")
                contatinho = int(input())
                lista_de_contatos.append(Contato(nomeF, numero, contatinho))
                lista_de_contatos = exibirNomesAlfabetica(lista_de_contatos)
            except:
                print("Entrada inválida")

        if opcao == 1:
            print("Digite o nome do contato a ser excluido:")
            nome = input()
            naAgenda = False
            for i in lista_de_contatos:
                if nome == i.nome:
                    naAgenda = True
                    lista_de_contatos.remove(i)
                    print("Removido com sucesso")
                    break
            if naAgenda == False:
                print("O contato não existe")

        if opcao == 2:
            correto = False
            while correto == False:
                print("1 - Exibir agenda completa")
                print("2 - Exibir apenas contatinho")
                n = input()
                try:
                    n = int(n)
                    if n == 1 or n == 2:
                        correto = True
                    else:
                        print("Numero incorreto")
                except:
                    print("Numero incorreto")
            for i in lista_de_contatos:
                if n == 2:
                    if i.contatinho == 1:
                        print(i.nome)
                        print("Numero de mensagens salvas:", len(i.mensagem))
                        for j in range(len(i.mensagem)):
                            print(i.mensagem[j])
                if n == 1:
                    print(i.nome)
            x = input()

        if opcao == 3:
            maisMsg = True
            while maisMsg:
                for i in lista_de_contatos:
                    if i.contatinho == 1:
                        print(i.nome)
                print("Para qual dos contatinhos gostaria de mandar mensagem?")
                nome = input()
                correto = False
                for i in lista_de_contatos:
                    if i.contatinho == 1 and nome == i.nome:
                        print("Digite a mensagem a ser enviada:")
                        msg = input()
                        msg = msg.replace("a", "1")
                        msg = msg.replace("e", "2")
                        msg = msg.replace("i", "3")
                        msg = msg.replace("o", "4")
                        msg = msg.replace("u", "5")
                        print(i.receberMensagem(msg))
                        correto = True
                        print("Deseja enviar mais outra mensagem?")
                        print("1 - sim")
                        print("2 - não")
                        try:
                            var = int(input())
                            if var == 2:
                                maisMsg = False
                        except:
                            print("Entrada invalida")
                if correto == False:
                    print("O contato não existe")

        if opcao == 9:
            salva_contatos()
            noMenu = False

    except:
        print("Entrada invalida")