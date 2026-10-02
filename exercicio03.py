numero = int(input("Digite um número de 1 a 10: "))

if 1 <= numero <= 10:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido! Digite um valor de 1 a 10.")
