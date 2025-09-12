#Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

print('==== 2. TypeError')
try:
  n = int(input('Ingresa un número: '))
  p = input('Ingresa una palabra: ')
  print(f'El resultado es: {n+p}')
except TypeError:
  print('Error! No se puede sumar una cadena de texto')

print('\n======Impresión en Consola: ')
n = 10
p = 'Palabra'
print(n+p)