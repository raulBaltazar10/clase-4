import time # Se importa la libreria time para dar descansos entre una funcion y otra

def linea_espera(time_sec):
    for i in range(0, time_sec):
        print('-', end=' ')
        time.sleep(1)

user = input('Dame tu nombre: ') # Se le solicita un dato al usuario
print('Procesando informacion')
linea_espera(5)

print(user) # Imprimimos el dato del usuario