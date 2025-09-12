#Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura
# la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

print('==== 1. ZeroDivisionError')
try:
  n1 = int(input('Ingresa 1er número: '))
  n2 = int(input('Ingresa 2do número: '))
  print(f'El resultado es: {n1/n2}')
except ZeroDivisionError:
  print('Error! No se puede dividir por cero')


print('\n======Impresión en Consola: ')
n = int(input('Ingresa un número entero: '))
print(n/0)

