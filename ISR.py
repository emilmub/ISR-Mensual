import numpy as np
import matplotlib.pyplot as plt

def ISR(Tabla,Salario):
	'''
	Calcula el Impuesto Sobre la Renta para un salario mensual

	Tabla: Matriz con los datos relevantes para el calculo
	Salario: Salario mensual para el que deseamos calcular
	'''
	
	for fila in Tabla:
		if Salario <= fila[1] and Salario >= fila[0]:
			cargoFijo = fila[2]
			diferencia = Salario - fila[0]
			porcentaje = fila[3]
			ISR = cargoFijo + diferencia*porcentaje
			return ISR

Tabla = np.loadtxt('TablaMensual.csv',skiprows=1,delimiter = ',')

Impuesto = ISR(Tabla,30000)
print(Impuesto)

