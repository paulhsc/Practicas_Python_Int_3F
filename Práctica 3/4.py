print('4. Calcular el promedio de una lista de números usando args y un operador ternario\n')


def promedio(*numeros):
  prom = 0 if not numeros else sum(numeros) / len(numeros)
  return (prom)

def ingreso_de_datos():
  list_num=[]
  while True:
    num_add = int(input('Ingresa número [0 para terminar]: '))
    if num_add > 0: list_num.append(num_add)
    else:break
  return list_num

lista_terminada = ingreso_de_datos()
prom_final = promedio(*lista_terminada)
print(f'▷▷ El promedio de {lista_terminada} es: {prom_final: .2f}')
