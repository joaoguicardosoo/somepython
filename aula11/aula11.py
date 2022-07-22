# Operadores Relacionais - Aula 4

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)

# limite de idade
muito_jovem = 20
muito_velho = 30

if muito_jovem <= idade <= muito_velho:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')