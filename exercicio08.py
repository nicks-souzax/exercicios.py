produtos = [
    {"nome": "Notebook", "preco": 2500.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Teclado", "preco": 45.00}
]

for produto in produtos:
    if produto["preco"] > 50:
        print(produto["nome"])
