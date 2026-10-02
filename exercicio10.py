boletim = {}

while True:
    resposta = input("Deseja adicionar um aluno? (s/n): ").lower()

    if resposta != "s":
        break

    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    boletim[nome] = nota

for aluno, nota in boletim.items():
    if nota >= 6.0:
        print(f"{aluno}: Aprovado")
    else:
        print(f"{aluno}: Reprovado")
