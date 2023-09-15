lista_compras = []

while True:
    compras = input("Digite o item que você deseja comprar ou digite 'stop' (para parar): ")
    
    if compras == "stop":
        break
    
    lista_compras.append(compras)

print("Lista de compras:")
for item in lista_compras:
    print(item)