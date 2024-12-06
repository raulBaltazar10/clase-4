# Se importa la librería time para dar descansos entre una función y otra
import time

def linea_espera(time_sec):
  for i in range(0,time_sec):
    print('-', end='')
    time.sleep(1)
  print('')

# Se le solicita un dato al usuario
user = input('Dame tu nombre: ')

# Implementamos una linea de carga
print('Procesando informacion')
linea_espera(5)

# Imprimimos el dato del usuario
print(user)



