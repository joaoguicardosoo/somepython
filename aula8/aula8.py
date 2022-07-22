nome = 'Joao'
idade = 21
altura = 1.72
peso = 62.5
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')


print(f'{nome}, nasceu em {nascimento}, seu imc é {imc:.2f} e possui {altura} de altura.')
