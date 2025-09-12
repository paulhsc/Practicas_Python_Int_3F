#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError,
# captura la excepción y muestra un mensaje de error al usuario. Sin embargo también intenta crear el archivo si no existe.

n_ar = 'arc.txt'
print('\n==== 4. FileNotFoundError')
with open(n_ar) as archivo:
  datos = archivo.read()
  print(f'Los datos del archivo con: {datos}')