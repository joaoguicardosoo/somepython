# For/ Else in py

variavel = ['joao', 'joaozinho', 'nogueira']

comeca_com_j = False
for valor in variavel:
    print(valor)
    if valor.lower().startswith('J'):
        continue

else:
    print('Não existe uma palavra que começa com J.')
