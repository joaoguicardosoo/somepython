#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

res1 = int(input('Telefonou para a vítima? '))
res2 = int(input('Esteve no local do crime? '))
res3 = int(input('Mora perto da vítima? '))
res4 = int(input('Devia para a vítima? '))
res5 = int(input('Já trabalhou com a vítima? '))

res_total = res1+res2+res3+res4+res5

if res_total <=2:
    print('Suspeita')
elif res_total <=4:
    print('Cúmplice')
elif res_total == 5:
    print('Assassino')
else:
    print('Inocente')