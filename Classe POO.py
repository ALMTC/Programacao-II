class MyClass():
    i = 1234

    a = True

    nome = "Teste"

    def teste(self):

        if(self.a == True):
            print("Verdadeiro")
        else:
            print("Falso")

    def hello(self):
        print("hello word")

Obj = MyClass()
Obj2 = MyClass()

Obj.hello()

Obj.i = 54321
Obj2.a = False

print(Obj2.i)

Obj.teste()
Obj2.teste()