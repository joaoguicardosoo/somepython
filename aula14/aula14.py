num1 = input('digite um número: ')
num2 = input('digite outro número: ')


#isnumeric isdigit isdecimal
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('erro')


