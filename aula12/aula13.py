usuario = input('Digite seu usuario. ')
senha = input('Senha do usuário. ')

usuario_bd = 'joao'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Logado')
else:
    print('Usuario ou senha inválidos.')