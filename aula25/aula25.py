# desempacotamento de listas e py

lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,9,100]

n1, n2, *_ = lista

print(f'{n1}, {n2}, {_}.')
