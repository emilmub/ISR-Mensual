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
			print(fila[0],fila[1])
			return fila

Tabla = np.loadtxt('TablaMensual.csv',skiprows=1,delimiter = ',')

datos = ISR(Tabla,30000)

