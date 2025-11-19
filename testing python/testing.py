
import numpy as np

# 1: CREAR TABLERO 10X10:
# Se puede crear el tablero con una función, en la que definimos filas, columnas, y agua directamente, o sin agua.

def crear_tablero (filas = 10, columnas = 10, agua = "-"): # esto nos crea el tablero y directamente definimos el agua y podemos llamarlo más adelante.
	tablero = np.full((filas, columnas), agua)
	return tablero

# luego, tenemos que guardar la función en una variable:

tablero = crear_tablero()
print(crear_tablero)

# 2: Posición de barcos:
# COLOCAR EL PRIMER BARCO:
barco1 = [(0,1),(1,1)]

def colocar_barcos(tablero, barco):
	for pieza in barco:
			tablero[pieza] = "O"
		return tablero #porque la tenemos que llamar en local 
tablero = colocar_barcos(tablero, barco1)
print(tablero)


# COLOCAR EL SEGUNDO BARCO:
tablero = crear_tablero()
barco1 = [(0,1),(1,1)]
barco2 = [(1,3),(1,4),(1,5),(1,6)]
print(tablero)

for barco in [barco1, barco2]:
	tablero = colocar_barcos(tablero, barco)
		print("-" *10)
print(tablero)

# barco 3 y 4 es lo mismo, podemos hacerlo en 1 sola función: SUSTITUYE LAS O POR X:

#tablero para saber donde aplicar la función
# coordenada para saber dónde

def recibir_disparo(tablero, coordenada):
	if tablero[coordenada] == "O":
			tablero[coordenada] = "X" # aqui le dispara a un barco
			print("tocado")
	elif tablero[coordenada] == "-":
		tablero[coordenada] = "∼"
		print("agua")
	else:
		print("Ya has disparado aqui")

recibir_disparo(tablero,(1,3))
