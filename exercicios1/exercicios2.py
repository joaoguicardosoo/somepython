nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho < 4:
    print('Seu nome é menor que 4 caracteres.')
elif tamanho <= 7:
    print('Seu nome possui 6 ou menos caracteres.')
else:
    print('Seu nome é muito grande.')