import numpy as np 
import matplotlib.pyplot as plt


class Schedulling():

	def __init__(self, path):

		# Import data
		data = np.genfromtxt(path)
		
		# Numero de maquinas 
		number_of_machines = data[0,1]

		# (Indice, tiempo)
		TT = [row[1] for row in data][1:]

		number_of_works = len(TT)

		# Lista de tiempos 
		lista_tiempos = np.zeros(int(number_of_machines))

		# Define C
		self.C = set()

		# Indice de inicializacion
		j = 1

		# Por cada procesador, una lista donde guardar los trabajos asignados
		procesadores = [ [] for i in range(int(number_of_machines))]

		while j != number_of_works + 1:

			lista_tiempos, procesador = self.Tiempo_de_procesadores(j, lista_tiempos, number_of_machines, TT)

			procesadores[procesador].append(j-1)

			j +=1

		print()
		for num, tiempo in enumerate(lista_tiempos):

			print(f'El procesador {num + 1} termina sus tareas tras {tiempo} unidades ')
			print(f'Tareas asignadas al procesador {procesadores[num]}\n')			


	def Tiempo_de_procesadores(self, Tarea_j, lista_de_tiempos, num_procesadores, lista_de_trabajos):

		if np.all(lista_de_tiempos == 0):
			procesador_disponible = np.random.randint(num_procesadores)

			lista_de_tiempos[procesador_disponible] += lista_de_trabajos[0]
			
			return lista_de_tiempos, procesador_disponible

		else:
			Nuevo_tiempo_a_asignar = lista_de_trabajos[Tarea_j - 1]

			procesador_disponible = np.argmin(lista_de_tiempos)

			lista_de_tiempos[procesador_disponible] += Nuevo_tiempo_a_asignar

			return lista_de_tiempos,  procesador_disponible


if __name__ == '__main__':

	Path = 'instance_4.txt' 
	Schedulling(Path)
