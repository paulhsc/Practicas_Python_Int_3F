print('\033[1:30:41m='* 15, '\033[m')
a = {'parlantes', 'monitor', ' teclado', 'mouse'}
b = {'sofá', 'mesa', 'parlantes', 'televisor'}
print(f'A: {a}')
print(f'B: {b}')

print('\033[1:30:41m='* 15, '\033[m')
print('''1. Dados dos conjuntos, A y B, escribe un programa en Python que imprima 
los elementos que se encuentran en A o en B, o en ambos.''')

c = a | b
print(f'   ▷LA unión de A y B es: {c}')
#print(a.union(b))
print('\033[1:30:41m='* 15, '\033[m')
print('''2. Dados dos conjuntos, A y B, escribe un programa en Python que imprima
los elementos que se encuentran en A y en B.''')

inter = a & b
print(f'    ▷ La intersección de A y B es: {inter}')
#print(a.intersection(b))
print('\033[1:30:41m='* 15, '\033[m')
print('''3. Dados dos conjuntos, A y B, escribe un programa en Python que imprima
los elementos que se encuentran en A y en B.''')

comun = a ^ b
print(f'    ▷ Los valores comunes en A y B son: {comun}')
#print(a.symmetric_difference(b))
print('\033[1:30:41m='* 15, '\033[m')
print('''4.Dados un conjunto, A, escribe un programa en Python que imprima 
si el conjunto es un subconjunto de otro conjunto, B.''')
if a <= b: print('A es un subconjunto de B')
else: print('A <no> es un subconjunto de B')
#print(a.issubset(b))
print('\033[1:30:41m='* 15, '\033[m')
print('''5. Dados un conjunto, A, escribe un programa en Python que 
imprima el número de elementos del conjunto.''')
print('Los elementos del conjunto A son: ',len(a))