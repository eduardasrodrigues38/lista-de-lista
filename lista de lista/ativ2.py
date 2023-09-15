quant = int(input("Digite quantas palavras você quer na lista: "))
list_words = []

for x in range(0, quant):
    palavra = input("Digite a palavra: ")
    list_words.append(palavra)

list_long_words = []

for word in list_words:
    if len(word) > 5:
        list_long_words.append(word)

print("Palavras com mais de 5 letras:", list_long_words)

