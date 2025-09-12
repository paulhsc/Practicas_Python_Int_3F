#Escribe un programa que intente acceder a una clave que no existe en un diccionario.
# Si se produce una excepción KeyError, captura la excepción y muestra

print('==== 3. KeyError')
try:
  d = {'nombre': 'Juan','sexo': 'M'}
  d['edad'] = input('Ingresa su edad: ')
  print(d['apellido'])
except KeyError:
  print('Error! La Key no se no existe en el diccionario')

print('\n======Impresión en Consola: ')
d = {'nombre': 'Juan','sexo': 'M'}
print(d['edad'])