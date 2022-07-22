import copy

#d1 = {
#    'chave1' : 'valor',
#    'chave2' : 'outro valor',
#    'chave3' : 'Tupla',
#}
#
#for k, v in d1.items():
#    print(k, v)

clientes = {
    'cliente1' : {
        'nome' : 'Joao',
        'sobrenome' : 'Guilherme',
    },
    'cliente2' : {
        'nome' : 'diego',
        'sobrenome' : 'miranda',
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'{dados_k} = {dados_v}')

print('#################')

