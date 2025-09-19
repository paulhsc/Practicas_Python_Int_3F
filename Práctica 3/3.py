
print('3. Determinar si un número es par o impar\n')

def par_imp():
  num = int(input(f'Ingresa un número:  '))
  print(f'▷▷ {num} es PAR' if num%2 == 0 else f'{num} es IMPAR')
par_imp()
