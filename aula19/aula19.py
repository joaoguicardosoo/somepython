'''
while/else
contadores
acumuladores
'''
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:    # só sera executado se while for falso, break não executa else
    print('Acabou')
print("executadooo")