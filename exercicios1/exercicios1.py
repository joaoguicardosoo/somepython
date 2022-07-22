hora = input('Digite quantas horas são(0-23): ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite!')

else:
    print ('Por favor, digite um horário entre 0 e 23.')
