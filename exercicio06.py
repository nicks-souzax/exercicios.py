notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}

soma = 0
quantidade = 0

for valor in notas.values():
    soma += valor
    quantidade += 1

media = soma / quantidade
print(f"Média geral da turma: {media:.2f}")
