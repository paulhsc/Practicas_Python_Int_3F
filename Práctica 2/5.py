# Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la
# excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción
# ValueError. En cualquier caso, muestra un mensaje de error al usuario.

print('\n==== 5. ZeroDivisionError / ValueError')
try:
  n1 = int(input('Ingresa 1er num: '))
  n2 = int(input('Ingresa 2do num: '))
  print(n1/n2)
except ZeroDivisionError:
  print('Error! No se puede dividir por cero')
except ValueError:
  print('Error! Tiene que ingresar un número entero')


print('\n======Impresión en Consola: ')

n1 = int(input('Ingresa 1er num (decimal para ValueError): '))
n2 = int(input('Ingresa 2do num (0 para ZeroDivisionError): '))
print(n1/n2)