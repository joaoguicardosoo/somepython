
perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Quanto é 2+2?',
        'respostas' : { 'a': '1', 'b': '4',  'c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5x6?',
        'respostas': {'a': '4', 'b': '10', 'c': '30'},
        'resposta_certa' : 'c',
    }
}
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!!')
        respostas_certas += 1
    else:
        print('Você errou!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')