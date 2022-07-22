"""
:s - texto
:d - inteiros
:f - números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro

"""

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'joao'
sobrenome = 'guilherme'
nome_formatado = '{0} {1:#^50}'. format(nome, sobrenome)
print(nome_formatado)


print(nome.lower())  # minusculo
print(nome.upper())  # maiusculo
print(nome.title())  # first maiuscula

print(nome.__reversed__())