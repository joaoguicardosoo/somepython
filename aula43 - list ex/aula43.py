import string


lista = '0123456789012345678901234567890123456789'
n = 10
comp = [lista[i:i+n] for i in range(0, len(lista), n)]
componto = '.'.join(comp)

print(componto)