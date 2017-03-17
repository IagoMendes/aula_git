def ler_numeros(n):
    lista=[]
    for i in range(n):
        numbers=float(input("Digite um número real: "))
        lista.append(numbers)
    return lista

lista=ler_numeros(10)
print(lista)


        
