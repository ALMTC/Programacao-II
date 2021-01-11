import pickle

noMenu = True
lista_livros = []
lista_usuarios = []


def salva_arquivo():
    arquivo = open("livros.txt", "w+b")
    pickle.dump(lista_livros, arquivo)
    arquivo.close()
    arquivo = open("user.txt", "w+b")
    pickle.dump(lista_usuarios, arquivo)
    arquivo.close()


class Usuario:
    def __init__(self, tipo, id):
        self.id = id
        self.tipo = tipo
        self.alugados = 0
        self.lista_alugada = []
        if self.tipo == 1:
            self.limite = 1
        else:
            self.limite = 3


class Livro:
    id = 0
    def __init__(self, nome):
        self.nome = nome
        self.alugado = False
        self.id = Livro.id
        Livro.id += 1


try:
    arquivo = open("livros.txt", "rb")
    lista_livros = pickle.load(arquivo)
    arquivo.close()
    arquivo = open("user.txt", "rb")
    lista_usuarios = pickle.load(arquivo)
    arquivo.close()
except:
    print("Sem dados anteriores salvos")

x = len(lista_livros)
Livro.id = lista_livros[x-1].id+1


while (noMenu):
    print("-" * 5 + "Bem vindo a Biblioteca" + "-" * 5)
    print("0 - Cadastrar livro")
    print("1 – cadastrar usuário")
    print("2 – consultar acervo")
    print("3 – alugar livro")
    print("4 – retornar livro")
    print("9 – sair da aplicação")
    opcao = (input())
    try:
        opcao = int(opcao)
        if opcao == 0:
            print("Digite o nome do livro:")
            nome = input()
            nome.upper()
            lista_livros.append(Livro(nome))
            print("Cadastro realizado")

        if opcao == 1:
            print("1 - Cadastrar aluno")
            print("2 - Cadastrar professor")
            cad = int(input())
            if cad == 1 or 2:
                print("Digite a matrícula:")
                matricula = int(input())
                jaExiste = False
                for i in lista_usuarios:
                    if matricula == i.id:
                        jaExiste = True
                if jaExiste:
                    print("Usuário já cadastrado")
                else:
                    lista_usuarios.append(Usuario(cad, matricula))
                    print("Cadastro realizado")
            else:
                print("Entrada invalida")

        if opcao == 2:
            escolher = True
            while escolher:
                print("Escolha uma das opções")
                print("1 - Acervo completo")
                print("2 - Livros disponíveis")
                print("3 - Livros alugados")
                escolha = int(input())
                if escolha == 1 or 2 or 3:
                    escolher = False
                else:
                    print("Entrada invalida")

            if len(lista_livros) > 0:
                for i in lista_livros:
                    if escolha == 1:
                        print(i.nome)
                    if escolha == 2 and i.alugado == False:
                        print(i.nome)
                    if escolha == 3 and i.alugado:
                        print(i.nome)
            else:
                print("Nem um livro cadastrado")

        if opcao == 3:
            print("Digite sua matrícula:")
            matric = int(input())
            for i in lista_usuarios:
                if matric == i.id:
                    user = i
            try:
                if user.limite > user.alugados:
                    for i in lista_livros:
                        if i.alugado == False:
                            print("nome:", i.nome, "matríula:", i.id)
                    print("Digite a matrícula do livro a ser alugado")
                    esc = int(input())
                    for i in lista_livros:
                        if i.id == esc:
                            i.alugado = True
                    user.alugados += 1
                    user.lista_alugada.append(esc)
                    print("Livro alugado com sucesso")
                else:
                    print("Usuário já alugou o máximo de livros simultaneos")
            except:
                print("Matricula invalida")

        if opcao == 4:
            print("Digite sua matrícula:")
            matric = int(input())
            user = 0
            for i in lista_usuarios:
                if matric == i.id:
                    user = i
            if user != 0:
                for id in user.lista_alugada:
                    for livro in lista_livros:
                        if id == livro.id:
                            livro.alugado = False
                user.alugados = 0
                user.lista_alugada = []
                print("Todos os livros foram devolvidos")
            else:
                print("Usuário invalido")

        if opcao == 9:
            salva_arquivo()
            noMenu = False
    except:
        pass