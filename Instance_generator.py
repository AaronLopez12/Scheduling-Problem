import numpy as np
import sys

def Create_instance(id):
	
	n = int(input("Número de máquinas de procesamiento: "))
	m = int(input("Número de tareas de la instancia: "))

	if n <= 0 and m <= 0:

		return 0

	else: 

		Instancia = np.zeros((m + 1, 2))
		Instancia[0,1] = n

		for tarea in range(1, m + 1):
			Instancia[tarea,0] = tarea	
			Instancia[tarea,1] = np.random.randint(1, 15)

		np.savetxt(f'instance_{id}.txt', Instancia, fmt='%d')



if __name__ == '__main__':
	Create_instance(int(sys.argv[1]))