nome = 'joao'
idade = 32 #int
altura = 1.80 #float
e_maior = idade > 18 #bool
peso = 62
imc = peso / altura ** 2

print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
