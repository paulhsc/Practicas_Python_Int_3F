print('2. Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario\n')

def buscar_pbra(*palabras):
  pbra = input('Qué palabra quieres buscar?: ').upper()
  rsp = f'{pbra} está en la lista' if pbra in palabras else f'{pbra} no está en la lista'
  return rsp

pbras_add = input('Ingresa varias palabras separados por espacio: \n').upper().split()
rsul_pbras_add =  buscar_pbra(*pbras_add)
print('▷▷',rsul_pbras_add)

