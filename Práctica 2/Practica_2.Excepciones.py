n = 10
p = 'Palabra'
d = {'nombre': 'Juan','sexo': 'M'}
n_ar = 'arc.txt'

print('==== 1.')
#print(n/0)

print('\n==== 2.')
#print(n+p)

print('\n==== 3.')
#print(d['edad'])
'''
print('\n==== 4.')
with open(n_ar) as archivo:
  datos = archivo.read()
  print(f'Los datos del archivo con: {datos}')
'''
print('\n==== 5.')

n1 = int(input('Ingresa 1er num (decimal para ValueError: '))
n2 = int(input('Ingresa 2do num(0 para ZeroDivisionError: '))
print(n1/n2)