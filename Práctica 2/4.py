#Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError,
# captura la excepción y muestra un mensaje de error al usuario. Sin embargo también intenta crear el archivo si no existe.

print('\n==== 4. FileNotFoundError')
n_ar = 'arc.txt'
try:
  with open(n_ar, 'r') as archivo:
    datos = archivo.read()
    print(f'Los datos del archivo con: {datos}')
except FileExistsError:
  print(f'Error! El archivo {n_ar} no fue encontrado')
