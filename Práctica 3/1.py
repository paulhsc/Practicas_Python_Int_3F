
print('1. Calcular el mayor de dos números ingresados por teclado usando un operador ternario')

def mayor():
  n1 = int(input('Ingresa un número: '))
  n2 = int(input('Ingresa otro número: '))
  print(f'▷▷ {n1} es mayor que {n2}' if n1 > n2 else f'{n2} es mayor que {n1}')
mayor()

