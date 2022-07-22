def saudacao(saudacao, nome):
    print(f'{saudacao}, {nome}')

saudacao('Olá', 'João')
saudacao('hey', 'john')

print('=================')

def soma(n1, n2, n3):
    print (n1 + n2 + n3)

soma(10, 20, 30)
soma(1,1,1)
soma(2,1,1)

print('=================')
def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual /100))

aumento_percentual(15, 20)

print('=================')
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 5 == 0:
        return 'buzz'
    elif n % 3 == 0:
        return 'fizz'
    else:
        return n

from random import randint

for i in range(10):
    aleatorio = randint(0, 10)
    print(fb(aleatorio))
