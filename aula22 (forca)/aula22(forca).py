# listas em python
# fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range

# booleanos = True
# inteiros = 10
# flutuante = -10.10
# strings = 'Textos'

# texto = 'Valor'
# lista = [1, 2, 3, 4, 'joao', True, 10.10]

#     0  1  2  3  4  5  6  7  8
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale , digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUU, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFF, a letra "{letra} não existe na palvra secreta.')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, vc ganhou!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f"Você ainda possui {chances} restantes.")