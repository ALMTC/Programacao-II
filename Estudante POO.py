gerar_aluno = True

class Estudante:
    countId = 0
    def __init__(self,n1,n2,):
        self.n1 = n1
        self.n2 = n2
        self.setID()

    def setID(self):
        self.__id = Estudante.countId
        Estudante.countId+=1

    def getID(self):
        return self.__id

a = Estudante(10,8)
b = Estudante(7,7)
c = Estudante(6,9)
d = Estudante(5,9)
e = Estudante(8,8)

print(a.getID(),b.getID(),c.getID(),d.getID(),e.getID())
