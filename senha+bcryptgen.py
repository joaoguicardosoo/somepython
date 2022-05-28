import random
import string
import bcrypt

lenght = int(input('Qual o tamanho da senha?'))

lower = string.ascii_lowercase                          ## puxa todos os elementos ASCII
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols                     ## concatena todos os elementos ASCII

temp = random.sample(all,lenght)                        ## gera aleatoriamente até o número de algarismos definido pelo usuário

password = "".join(temp)                                ## junta todos os gerados com nenhum espaçador

salt = bcrypt.gensalt()                                 # criptografando com bcrypt
hashed = bcrypt.hashpw(password.encode('utf-8'), salt)


print(f'Sua senha normal é: {password}')
print(f'Sua senha em bcrypt é: {salt} {hashed}')
