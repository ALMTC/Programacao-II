def contaLetras(str, a):
    count = 0
    for i in str:
        if i is a:
            count+=1
    return count

print("Digite a palavra a verificar")
palavra = input()
print("Digite a letra para verificar")
letra = input()

res = contaLetras(palavra, letra)
print("Se repete", res, "vezes")

https://www.spriters-resource.com/custom_edited/supersmashbroscustoms/sheet/25298/
