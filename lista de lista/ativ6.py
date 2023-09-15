quant = int(input("Digite a quantidade de numeros você quer na lista: "))
lista_numeros = []

for x in range(quant):
    numb = int (input("Digite o numero: "))
    lista_numeros.append(numb)

lista_sem_duplicatas = []
for elemento in lista_numeros:
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
    else:
        lista_numeros.remove(elemento)

print("Lista sem duplicatas:", lista_sem_duplicatas)