# add, update, clear, discard
# union
# intersection  &
# difference  -
# symmetric_difference  ^


s1 = set()
s1.add(1)
s1.add(2)
s1.add((1,2,3, 'Luiz'))

s1.discard(2)

print(s1)

l1 = ['Joao', 'Maria', 'Luis']
l2 = ['Maria', 'Joao', 'Luis', 'Luiz','Luiz','Luiz','Luiz',]

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L')