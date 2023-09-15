quant = int(input("Digite a quantidade de numeros você quer na lista: "))
list_numbers = []

for x in range(0, quant):
    numb = int (input("Digite a palavra: "))
    list_numbers.append(numb)

soma=sum(list_numbers)
print(soma)