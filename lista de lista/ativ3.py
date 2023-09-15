lista_num = [1, 2, 3, 4, 5]

tamanho = len(lista_num)
for i in range(tamanho /2):
    lista_num[i], lista_num[tamanho - 1 - i] = lista_num[tamanho - 1 - i], lista_num[i]

print(lista_num)