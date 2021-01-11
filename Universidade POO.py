"""""https://wiki.python.org.br/ListaDeExercicios"""

class Uni():
    def __init__(self, lista = [3,2,1]):
        self.lista = lista

    def disparaMensagem(self):
        for i in self.lista:
            print(i.nome)

class User():
    def __init__(self, pnome, pid):
        self.nome = pnome
        self.id = pid

class Professor(User):
    def __init__(self,pNome, pID, Nprovas=0):
        super().__init__(pNome, pID)
        self.provas = Nprovas
    def exibeMensagem(self):
        print(self.nome,"Provas para corrigir: ", self.provas)

class Aluno(User):
    def __init__(self,pNome, pID, nTD=0):
        super().__init__(pNome, pID)
        self.TDdeMAMI = nTD

    def exibeMesnsagem(self):
        print(self.nome,"Trabalhos de MAMI incompletos: " , self.TDdeMAMI)


Aluno1 = Aluno("aluno1", 101, 5)
Aluno2 = Aluno("aluno2", 102, 4)
Aluno3 = Aluno("aluno3", 103, 1)
Prof1 = Professor("prof1", 11, 12)
Prof2 = Professor("prof2", 12, 11)
Prof3 = Professor("prof3", 13, 11)
lista = [Aluno1, Aluno2, Aluno3, Prof1, Prof2, Prof3]

universidade = Uni(lista)
universidade.disparaMensagem()