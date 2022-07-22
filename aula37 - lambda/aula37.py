lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

caminho = input('Você quer listar em crescente? ')

if caminho == 'sim':
    print(sorted(lista, key=lambda i: i[1], reverse=False))
else:
    print(lista)
