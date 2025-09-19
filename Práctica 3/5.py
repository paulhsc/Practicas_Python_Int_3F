print('5. Imprimir un mensaje de error si no se pasan suficientes argumentos\n')

def sumar_num(*num_agr):
  if len(num_agr) < 2: print('▷▷ ERROR! Se necesitan al menos 2 valores para la suma.')
  else: print(f'▷▷ La suma de {num_agr} es: {sum(num_agr)}')
  return sum(num_agr)

def ingreso_de_datos():
  list_num=[]
  while True:
    num_add = int(input('Ingresa número [0 para terminar]: '))
    if num_add > 0: list_num.append(num_add)
    else:break
  return list_num

lista_terminada = ingreso_de_datos()
suma_final = sumar_num(*lista_terminada)