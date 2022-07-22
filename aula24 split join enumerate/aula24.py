#            split, join, enumerate
# split - dividir uma string # str
# join - juntar uma lista # str
# enumerate - enumerar elementos da lista # list

lista = [#0    #1      #2
    ['Luis', 'joao', 'maria'], # 0
    ['a', 'b', 'c'],           # 1
    ['d', 'e', 'f'],           # 2
]

for v1, v2 in enumerate(lista):
    print(v1, v2)
    