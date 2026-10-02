palavra = input("Digite uma palavra: ")
vogais = []

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais.append(letra)

print(vogais)
